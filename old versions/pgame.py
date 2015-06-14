#!/usr/bin/python

## imports

import sys
import pickle





#####################################################################
#
## classes
#
#####################################################################

testarray = []

class World(object):
    def __init__(self):
        self.name = "the world"
        self.object_count = 0
        pass

class Person(object):
    def __init__(self,name):
        self.name = name
        self.general_influence = 10
        self.money = 10
        self.personal_power = 10

    def sayhi(self):
        print "Congrats you have created a instance of a class called person",self.name
    def increase_value(characteristic):
        characteristic = characteristic + 10
    def increase_value(characteristic):
        characteristic = characteristic - 10

class Dictator(Person):
    def __init__(self,name):
        self.name = name
    def sayhello(self):
        print "Congrats you have a dictator named ", self.name

class Elected_Leader(Person):
    def __init__(self,name):
        self.name = name
    def sayhowdy(self):
        print "congrats you have created a freely elected leader named ",self.name

class PoliticalInteraction(object):
    def __init__(self, first_party, second_party):
        pass
    def theyaretalking(self):
        print "they are talking"
    
class Country(object):
    pass

class War(object):
    pass

class Military_Op(object):
    pass

######################################################################
#
##  the instances of the classes
#
######################################################################
 
print " If you want to start a new game type new, if you want to load an old game type game name", 
whichgame = raw_input()

if whichgame == "new":  
    world = World()
    test = Person("Chris")
    world.object_count += 1
    russian_dictator =Dictator("Vladimir")
    world.object_count += 1
    german_kanzler = Elected_Leader("Angie")
    world.object_count += 1
else:
    with open('people-pickle', "rb") as f:
        for _ in range(pickle.load(f)):
            testarray.append(pickle.load(f))
    world = testarray[0]
    test = testarray[1]
    russian_dictator = testarray[2]
    german_kanzler = testarray[3]

######################################################################
#
## the program
#
######################################################################

print "number of objects is ",  world.object_count
test.sayhi()
russian_dictator.sayhello()
russian_dictator.sayhi()
german_kanzler.sayhi()
german_kanzler.sayhowdy()

print "Would you like to save the game, y or n"
answer = raw_input()
if answer == "n":
    print "thanks for playing see you later gator"
elif answer == "y":
    dbfile = open('people-pickle', 'wb')               # use binary mode files in 3.X
    pickle.dump(4,dbfile)
    pickle.dump(world, dbfile)
    pickle.dump(test, dbfile)
    pickle.dump(russian_dictator, dbfile)              # data is bytes, not str
    pickle.dump(german_kanzler, dbfile)
    #pickle.dump(german_kanzler, dbfile)
    #pickle.dump(german_kanzler, dbfile)
    dbfile.close()
    print "we are working on that gator"



