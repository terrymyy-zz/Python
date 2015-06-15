import random
print "hello"
def print_intro():
    print """
Congrats, you are the newest ruler of ancient Samaria, elected for a ten year term
of office. Your duties are to distribute food, direct farming, and buy and sell land
as needed to support your people. Watch out for rat infestations and the resultant
plague! Grain is the general currency, measured in bushels. The following will help
you in your decisions:
            * Each person needs at least 20 bushels of grain per year to survive.
            * Each person can farm at most 10 acres of land.
            * It takes 2 bushels of grain to farm an acre of land.
            * The market price for land fluctuates yearly.
Rule wisely and you will be showered with appreciation at the end of your term. Rule
poorly and you will be kicked out of office!\n"""
    return

def Hammurabi():
    print_intro()

    starved            = 0
    immigrants         = 5
    population         = 100
    harvest            = 3000     # total bushels harveted
    bushels_per_acre   = 3# amount harvested for each acre planted
    rats_ate           = 200         # bushels destroyed by rats
    bushels_in_storage = 2800
    acres_owned        = 1000
    cost_per_acre      = 19    # each acre costs this many bushels
    plague_deaths      = 0

    for year in range(0,10):
        print 'O great Hammurabi!'
        print "You are in year " + str(year) + " of your ten year rule."
        print "In the previous year " + str(starved) +" people starved to death."
        print "In the previous year " + str(immigrants)+ " people entered the kingdom."
        print "The population is now " + str(population) + "."
        print "We harvested " + str(harvest) + " bushels at " + str(bushels_per_acre) + " bushels per acre."
        print "Rats destroyed " + str(rats_ate) + " bushels, leaving " + str(bushels_in_storage) + " bushels in storage."
        print "The city owns " + str(acres_owned) + " acres of land."
        print "Land is currently worth " + str(cost_per_acre) + " bushels per acre."
        print "There were "+ str(plague_deaths) +" deaths from the plague.\n"

        acres_buy = ask_to_buy_land(bushels_in_storage, cost_per_acre)
        if acres_buy <= 0 :
            acres_sell          = ask_to_sell_land(acres_owned)
            acres_owned        -= acres_sell
            bushels_in_storage += acres_sell * cost_per_acre
        else:
            acres_owned        += acres_buy
            bushels_in_storage -= acres_buy * cost_per_acre

        bushels_feed        = ask_to_feed(bushels_in_storage)
        bushels_in_storage -= bushels_feed
        starved             = numStarving(population, bushels_feed)

        acres_plant         = ask_to_cultivate(acres_owned, population, bushels_in_storage)
        acres_owned        -= acres_plant
        havest              = bushels_per_acre * acres_plant
        bushels_in_storage += harvest

    ############
        immigrants          = numImmigrants(acres_owned, bushels_in_storage, population, starved)
        cost_per_acre       = priceOfLand()

        population         -= starved
        population         += immigrants

        bushels_per_acre    = getHarvest()

        rats_ate            = bushels_in_storage * doRatsInfest()
        bushels_in_storage -= rats_ate

        if isPlague:
            plague_deaths = population/2
            population   -= plague_deaths

        # Due to this extreme mismanagement, you have not only been impeached and thrown out of office but you have also been declared 'National Fink'!!
        # A fantastic performance!!! Charlemagne, Disraeli and Jefferson combined could not have done better!
        # Your heavy-handed performance smacks of Nero and Ivan IV. The people (remaining) find you an unpleasant ruler, and, frankly, hate your guts!
    return

def ask_to_buy_land(bushels_in_storage, cost_per_acre):
    '''Ask user how many bushels to spend buying land.'''
    acres_buy = input("How many acres will you buy? ")
    while acres_buy * cost_per_acre > bushels_in_storage:
        print "O great Hammurabi, we have but", bushels_in_storage, "bushels of grain!"
        acres_buy = input("How many acres will you buy? ")
    return acres_buy

def ask_to_sell_land(acres_owned):
    '''Ask user how much land they want to sell. '''
    acres_sell = input("How many acres will you sell? ")
    while acres_sell > acres_owned:
        print "O great Hammurabi, we have but", acres_owned, "acres of land!"
        acres_sell = input("How many acres will you sell? ")
    return acres_sell

def ask_to_feed(bushels_in_storage):
    '''Ask user how many bushels they want to use for feeding. '''
    bushels_feed = input("How much grain to feed the people? ")
    while bushels_feed > bushels_in_storage:
        print "O great Hammurabi, we have but", bushels_in_storage, "bushels of grain!"
        bushels_feed = input("How much grain to feed the people? ")
    return bushels_feed

def ask_to_cultivate(acres_owned, population, bushels_in_storage):
    '''Ask user how much land they want to plant seed in'''
    acres_plant = input("How many acres to plant with seed? ")
    while acres_plant > acres_owned:
        print "O great Hammurabi, we have just", acres_owned, "acres owned!"
        acres_plant = input("How many acres to plant with seed? ")
    while acres_plant > bushels_in_storage:
        print "O great Hammurabi, we have just", bushels_in_storage, "bushels in storage!"
        acres_plant = input("How many acres to plant with seed? ")
    while acres_plant > population*10:
        print "O great Hammurabi, we have just", population, "people!"
        acres_plant = input("How many acres to plant with seed? ")
    return acres_plant

def isPlague():
    if random.randint(1, 100) > 85:
        return True
    else:
        return False

def numStarving(population, bushels_feed):
    starved = population - bushels_feed / 20.0
    if starved / population > 0.45:
        print "You've been kicked out of office!"
        print "You starved ", int(starved), " people in one year!"
        exit(0)
    elif starved < 0:
        starved = 0
    return int(starved)

def numImmigrants(acres_owned, bushels_in_storage, population, starved):
    if starved > 0:
        immigrants = 0
    else:
        immigrants = (20 * acres_owned + bushels_in_storage) / (100 * population + 1)
    return immigrants

def getHarvest():
     return random.randint(1, 8)

def doRatsInfest():
    if random.randint(1, 100) > 40:
        return 0
    else:
        return random.randint(10, 30)/100.0

def priceOfLand():
    return random.randint(16, 22)
