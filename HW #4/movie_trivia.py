import csv

def create_actors_DB(actor_file):
    '''Create a dictionary keyed on actors from a text file'''
    f = open(actor_file)
    movieInfo = {}
    for line in f:
        line = line.rstrip().lstrip()
        actorAndMovies = line.split(',')
        actor = actorAndMovies[0].lower()
        movies = [x.lstrip().rstrip().lower() for x in actorAndMovies[1:]]
        movieInfo[actor] = set(movies)
    f.close()
    return movieInfo

def create_ratings_DB(ratings_file):
    '''make a dictionary from the rotten tomatoes csv file'''
    scores_dict = {}
    with open(ratings_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            scores_dict[row[0].lower()] = [row[1], row[2]]
    return scores_dict

def insert_actor_info(actor, movies, movie_Db):
    '''Insert actor and his movies info'''
    if actor in movie_Db.keys():
        movie_Db[actor].update(movies)
    else:
        movie_Db.update({actor:movies})
    return

def insert_rating(movie, ratings, ratings_Db):
    '''Insert new ratings of a movie'''
    ratings_Db.update({movie:ratings})
    return

def delete_movie(movie, movie_Db, ratings_Db):
    '''Delete a movie's rating and its actors' infos'''
    del ratings_Db[movie]
    for actor in movie_Db:
        movie_Db[actor].discard(movie)
    return

def select_where_actor_is(actorName, movie_Db):
    '''Given a actor name, return his movies'''
    return list(movie_Db[actorName])

def select_where_movie_is(movieName, movie_Db):
    '''Given a movie name, return its actors'''
    movie_actors = []
    for actor in movie_Db.keys():
        if movieName in movie_Db.get(actor):
            movie_actors.append(actor)
    return movie_actors

def select_where_rating_is(targeted_rating, comparison, is_critic, ratings_Db):
    '''Given the targeted_rating and comparison, whether from critics or audience,
    compare the ratings to targeted_rating then return the movies meets the requirement'''
    movies = list()
    index  = 1
    if is_critic:
        index = 0
    for movie in ratings_Db:
        if comparison == '>' and int(ratings_Db.get(movie)[index]) > targeted_rating:
            movies.append(movie)
        elif comparison == '=' and int(ratings_Db.get(movie)[index]) == targeted_rating:
            movies.append(movie)
        elif comparison == '<' and int(ratings_Db.get(movie)[index]) < targeted_rating:
            movies.append(movie)
    return movies

def get_co_actors(actorName, moviedb):
    '''Given an actor name, return all the actors he had cooperated with.'''
    movies = moviedb.get(actorName)
    actors = []
    for actor in moviedb.keys():
        if len(movies.intersection(moviedb[actor])) != 0:
            actors.append(actor)
    actors.remove(actorName)
    return actors

def get_common_movie(actor1, actor2, moviedb):
    '''Given 2 actors, find the movie they have been cooperated in'''
    movies1 = moviedb.get(actor1)
    movies2 = moviedb.get(actor2)
    return list(movies1.intersection(movies2))

def critics_darling(movie_Db, ratings_Db):
    '''Given two databse, return the favorite list of critics'''
    average = []
    for actor in movie_Db.keys():
        average.append(get_actor_average(actor,True,movie_Db,ratings_Db))
    critics_darling = get_average_names(average)
    return critics_darling

def audience_darling(movie_Db, ratings_Db):
    '''Given two databse, return the favorite list of average'''
    average = []
    for actor in movie_Db.keys():
        average.append(get_actor_average(actor,False,movie_Db,ratings_Db))
    audience_darling = get_average_names(average)
    return audience_darling

def get_actor_average(actorName,is_critic,movie_Db,ratings_Db):
    '''This function helps to calculate the average rating of a given actor'''
    ratings = []
    average = []
    index = 1
    if is_critic:
        index = 0
    for movie in movie_Db[actorName]:
        if movie in ratings_Db.keys():
            ratings.append(int(ratings_Db.get(movie)[index]))
    average = [sum(ratings)/float(len(ratings)),actorName]
    return average

def get_average_names(average):
    '''This function helps to sort the actors in the order of average ratings,
    then return the list of darling'''
    darling = []
    average.sort(reverse = True)
    for item in average:
        darling.append(item[1])
    return darling

def good_movies(ratings_Db):
    '''Given ratings_Db, return the movies those critics and 
    audience all have positive response'''
    movies = set()
    critics_movies = set()
    audience_movies = set()

    critics_movies.update(select_where_rating_is(85, '>', True, ratings_Db))
    audience_movies.update(select_where_rating_is(85, '>', False, ratings_Db))

    movies = critics_movies.intersection(audience_movies)
    return movies

def get_common_actors(movie1, movie2, movie_Db):
    '''Given a pair of movies, return a list of actors that acted in both.'''
    actors1 = select_where_movie_is(movie1, movie_Db)
    actors2 = select_where_movie_is(movie2, movie_Db)
    common_actors = set(actors1).intersection(set(actors2))
    return list(common_actors)

def print_instruction():
    '''Print out user instructions'''
    print 'Welcome! This is a database of actors infos and movies ratings!\n'
    print 'Press 1 for movies of an actor or actress'
    print 'Press 2 for actors and actresses of a movie'
    print 'Press 3 to find movies of a rating range you like'
    print 'Press 4 to find all actors that an actor had collabrated with'
    print 'Press 5 to find which movie(s) two actors had joined?'
    print "Press 6 for a list of critics' favorite actors"
    print "Press 7 for a list of audience' favorite actors"
    print 'Press 8 for movies both audience and critics rate above 85'
    print 'Press 9 for actors appeared in certain two movies'
    print 'Press 10 for adding actor and movie infos'
    print 'Press 11 for adding rating infos'
    print 'Press 12 for deleting movie infos from database'
    print 'Press 0 to quit'

def all_movies(movie_Db):
    '''list all the movies out'''
    all_movies = set()
    for actor in movie_Db:
        all_movies.update(movie_Db.get(actor))
    return list(all_movies)

def main():
    actor_DB = create_actors_DB('movies.txt')
    ratings_DB = create_ratings_DB('moviescores.csv')
    
    print_instruction()
    choice = input("What's your choice? Please enter a number:\n")
    while choice != 0:
        if choice == 1:
            actorName = raw_input('Please enter the name of the actor:\n').lower()
            if actorName in actor_DB.keys():
                print select_where_actor_is(actorName,actor_DB)
            else:
                print 'Not present!'

        if choice == 2:
            movieName = raw_input('Please enter the name of the movie:\n').lower()
            actors = select_where_movie_is(movieName,actor_DB)
            if actors == []:
                print 'Not present!'
            else:
                print 'Actors in ', movieName, ' are as follows:\n'
                print actors

        if choice == 3:
            targeted_rating = input('Please enter a target rating: \n')
            comparison = raw_input("Please enter a comparison: '=','>' or '<'\n")
            rating_choice = raw_input("Press 'c' for critics rating, 'a' for audience rating\n")
            if rating_choice == 'c':
                is_critic = True
            else:
                is_critic = False
            
            print "The movies in your range are listed below:\n"
            print select_where_rating_is(targeted_rating,comparison,is_critic,ratings_DB)

        if choice == 4:
            actorName = raw_input('Please enter the name of the actor: \n').lower()
            if actorName in actor_DB.keys():
                co_actors = get_co_actors(actorName,actor_DB)
                print 'The actors collabrated with ',actorName, 'are listed as follow:\n'
                print co_actors
            else:
                print 'Not present!'

        if choice == 5:
            actor1 = raw_input('Please enter the name of the 1st actor:\n').lower()
            actor2 = raw_input('Please enter the name of the 2nd actor:\n').lower()
            if actor1 and actor2 not in actor_DB.keys():
                print "Sorry actors not present!"
            else :
                common_movie = get_common_movie(actor1,actor2,actor_DB)
                print "The movies in which ",actor1, ' and ',actor2, 'collabrated are listed as follows:\n'
                print common_movie

        if choice == 6:
            print "Here is the critics' favorite list of actors:\n"
            print critics_darling(actor_DB,ratings_DB)

        if choice == 7:
            print "Here is the audiences' favorite list of actors:\n"
            print audience_darling(actor_DB,ratings_DB)

        if choice == 8:
            print 'This is the list that both audiences and critics have rated above 85:\n'
            print good_movies(ratings_DB)

        if choice == 9:
            movie1 = raw_input('Please enter the 1st movie:\n').lower()
            movie2 = raw_input('Please enter the 2nd movie:\n').lower()
            all_movie = all_movies(actor_DB)
            if movie1 and movie2 not in all_movie:
                print 'Sorry! 1st or 2nd movie not present!'
            else:
                print 'The common actors in these two movies are listed as below:\n'
                print get_common_actors(movie1,movie2,actor_DB)

        if choice == 10:
            actor = raw_input('Please enter the name of actor to add:\n').lower()
            movies = raw_input('Please enter a list of movies of him:\n').lower()
            movies = movies.split(',')
            insert_actor_info(actor,movies,actor_DB)
            print 'Your info has been added into database! Thank you!'

        if choice == 11:
            movie = raw_input('Please enter the movie name to add:\n').lower()
            critic_rating = input('Please enter rating of this movie by the critics (0-100):\n')
            audience_rating = input('Please enter rating by the audience:(0-100)\n')
            ratings = critic_rating,audience_rating
            insert_rating(movie,ratings,ratings_DB)
            print 'Your info has been added into database! Thank you!'

        if choice == 12:
            movie = raw_input('Please enter the movie name you want to delete:\n').lower()
            delete_movie(movie,actor_DB,ratings_DB)
            print 'The info about the movie ',movie,'has been removed!'

        if choice == 0:
            print 'Thanks for using this database!'
            break

        if choice not in range(0,13):
            choice = input('Please re-enter a number(0~12):\n')

        print_instruction()
        choice = input('If you want to continue, enter a number(1~12,0 for quit):\n')
        

if __name__ == '__main__':
    main()