from movie_trivia import *
import unittest

class TestMovies(unittest.TestCase):
    
    movieDb  = {}
    ratingDb = {}

    def setUp(self):
        self.movieDb  = create_actors_DB('movies.txt')
        self.ratingDb = create_ratings_DB('moviescores.csv')

    def testselect_where_movie_is(self):
        #write test code here using self.ratingDb and self.movieDb
        actors = set(select_where_movie_is('jfk', self.movieDb))
        #make some assertion about these actors
        self.assertEqual(set(['kevin bacon','kevin costner']), actors)
        
        actors2 = select_where_movie_is('asdfadsfafaf', self.movieDb)
        self.assertFalse(len(actors2)!=0)

    def testinsert_actor_info(self):
        # Test an actor that is already exist in the Dictionary,
        # add movies to his set and check whether they are created.
        actor  = 'jim carrey'
        movies = ['the truman show', 'liar liar']
        insert_actor_info(actor,movies,self.movieDb)
        self.assertTrue(movies[0] in self.movieDb[actor])
        self.assertTrue(movies[1] in self.movieDb[actor])
        # Test an actor that is not in the Dictionary
        # Add the actor and his movies in the Dictionary
        actor1  = 'yaoyu ma'
        movies1 = ['123 I love you', 'No No I like python']
        insert_actor_info(actor1,movies1,self.movieDb)
        self.assertTrue(movies1[0] in self.movieDb[actor1])
        self.assertTrue(movies1[1] in self.movieDb[actor1])

    def testinsert_rating(self):
        # Test insert rating by insert a movie rating and see whether rating 
        # in ratingDb or not
        movie  = 'go to the west'
        rating = (79,88)
        insert_rating(movie,rating,self.ratingDb)
        self.assertTrue(movie in self.ratingDb.keys())
        self.assertEqual(rating, self.ratingDb[movie])

    def testdelete_movie(self):
        # Test whether all movie infos in ratingDb and movieDb are removed
        movie  = 'sound of music'
        delete_movie(movie, self.movieDb, self.ratingDb)
        self.assertTrue(movie not in self.ratingDb.keys())
        for actor in self.movieDb:
            self.assertTrue(movie not in self.movieDb[actor])

    def testselect_where_actor_is(self):
        # Test whether this function can return all the movie the actor acted
        actor  = 'brad pitt'
        self.assertEqual(select_where_actor_is(actor,self.movieDb), list(self.movieDb[actor]))

    def testselect_where_rating_is(self):
        # Test whether the function can select a rating range of movies
        self.assertEqual(select_where_rating_is(0,'>',True,self.ratingDb), self.ratingDb.keys())
        self.assertEqual(select_where_rating_is(65,'=',False,self.ratingDb), ['star wars'])
        self.assertEqual(set(select_where_rating_is(30,'<',True,self.ratingDb)), set(['lara croft tomb raider', 'bone collector', 'wild wild west', 'original sin', 'assassins']))

    def testget_co_actors(self):
        # Test whether whether can find co_actor with 'brad pitt'
        actors = set(['anthony hopkins', 'angelina jolie', 'dustin hoffman', 'kevin bacon', 'morgan freeman', 'george clooney', 'eric bana', 'julia roberts', 'diane kruger'])
        self.assertEqual(set(get_co_actors('brad pitt', self.movieDb)), actors)

    def testget_common_movie(self):
        # Test whether get common movie two actors have
        common_movie = get_common_movie('angelina jolie', 'brad pitt', self.movieDb)
        self.assertTrue('mr & mrs smith' in common_movie)
        self.assertFalse('sound of music' in common_movie)
        common_movie1 = get_common_movie('jim carrey', 'brad pitt', self.movieDb)
        self.assertTrue(common_movie1 == [])

    def testcritics_darling(self):
        # Test whether can generate a critics favorite list
        self.assertEqual(critics_darling(self.movieDb,self.ratingDb)[0],'joan fontaine')

    def testaudience_darling(self):
        # Test whether can generate a audience favorite list
        self.assertEqual(audience_darling(self.movieDb,self.ratingDb)[0],'diane keaton')

    def testget_actor_average(self):
        # Test helper function: give an actor, get the average rating
        self.assertEqual(get_actor_average('brad pitt', True, self.movieDb,self.ratingDb)[0],66.5)
        self.assertEqual(get_actor_average('angelina jolie', False, self.movieDb,self.ratingDb)[0],57.0)

    def testget_average_names(self):
        # Test helper function: give an average list, sort by the ratings
        list1 = [[1.2, 'terry'], [8.9, 'ghjgj'], [5.6, 'asdfasd']]
        self.assertEqual(get_average_names(list1),['ghjgj','asdfasd','terry'])

    def testgood_movies(self):
        # Test whether good movie is in the result

        self.assertTrue('kramer vs. kramer' in good_movies(self.ratingDb))

    def testget_common_actors(self):
        # Test whether can get actors from two movies
        actors = get_common_actors('sleepers', 'troy', self.movieDb)
        self.assertEqual(actors, ['brad pitt'])

    def testall_movies(self):
        # Test helper function: get all the movies
        self.assertEqual(len(all_movies(self.movieDb)), 271)
        self.assertTrue('mr & mrs smith' in all_movies(self.movieDb))
        self.assertFalse('asdfasdfasdf' in all_movies(self.movieDb))

    #write unit tests for every function.
             
unittest.main()
