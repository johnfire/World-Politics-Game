#!/usr/bin/python3

## imports

import sys
import pickle
from game_classes import *
#from python3-pyside.qtcore import *
#from PySide.QtGui import *
#from python3-PyQt4.Qt import *
#this all costs massive amounts of money. no point in buying stuff if you can get it for free... tkinter may be the way to go


## variables, lists, etc

#human agents in the game

peeps = []
tyrants = []
elected_types = []
religous_types =[]

#countries, areas cities etc

countries = []
areas = []
cities = []
towns = []
oceans = []
seas = []

#government, non government organizations etc

governments = []
ngos = []
interest_groups = []
companies = []

#actions by human agents in game

actions = []


# added as a test for verson control
#
#
#


######################################################################
#
##  the instances of the classes
#
######################################################################
 
 
print (" If you want to start a new game type new, if you want to load an old game type game name"), 
whichgame = input()

if whichgame == "new":  
    world = World()
    peeps.append(Person("Chris"))
    world.object_count += 1
    world.peeps_count += 1
    tyrants.append(Dictator("Vladimir"))
    world.object_count += 1
    world.tyrants_count += 1
    elected_types.append(Elected_Leader("Angie"))
    world.object_count += 1
    world.elected_types_count += 1
else:
    with open('people-pickle', "rb") as f:
        world = pickle.load(f)
        for x in range(0, world.peeps_count):
            peeps.append(pickle.load(f))
        for x in range(0, world.tyrants_count):
            tyrants.append(pickle.load(f))
        for x in range(0, world.elected_types_count):
            elected_types.append(pickle.load(f))

######################################################################
#
## the program
#
######################################################################

print ("number of objects is ",  world.object_count)

for x in range(0, world.peeps_count):
    peeps[x].sayhi()    
for x in range(0, world.tyrants_count):
    tyrants[x].sayhello()
    tyrants[x].sayhi()	
for x in range(0, world.elected_types_count):
    elected_types[x].sayhowdy()
    elected_types[x].sayhi()


print ("would you like to create a new person in the world")
answer = input()

while answer == "y":
    print ("enter the name please",) 
    name = input()
    print ("select type 1 = person 2 = dictator 3 = elected leader")
    type = input()
    if type == "1":
        peeps.append(Person(name))
        world.object_count += 1
        world.peeps_count += 1
    elif type == "2":
        tyrants.append(Dictator(name))
        world.object_count += 1
        world.tyrants_count += 1
    elif type == "3":
        elected_types.append(Elected_Leader(name))
        world.object_count += 1
        world.elected_types_count += 1
    elif type == "4":
        religous_peeps.append(Person(name))
        world.object_count += 1
        world.religous_types_count += 1
    print ("Would you like to create another?")
    answer = input()

print ("Halt here for a minute. Type anything to continue")
answer = input()
print ("\n")

print (" number of objects ", world.object_count)        
print ("Would you like to save the game, y or n")
answer = input()

if answer == "n":
    print ("thanks for playing see you later gator")
elif answer == "y":
    dbfile = open('people-pickle', 'wb')               # use binary mode files in 3.X
    pickle.dump(world, dbfile)
    for x in range (0, world.peeps_count):
        pickle.dump(peeps[x], dbfile)
    for x in range (0, world.tyrants_count):
        pickle.dump(tyrants[x], dbfile)              # data is bytes, not str
    for x in range(0, world. elected_types_count):
        pickle.dump(elected_types[x], dbfile)
    dbfile.close()
    print ("we are working on that gator, right now it works... lets see what happens next.")

print ("ok see you later....")


