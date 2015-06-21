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
religous_types = []

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

#conflict area list

interestareas =[]

# added as a test for verson control
#addes again as test for version contrl june 21 2015
#
#

######################################################################
#
##  the instances of the classes
#
######################################################################
 

######################################################################
#
#game functions
#
######################################################################

def gameloop ():
    print ("In the loop")
    print ("The time is ",world.time)
    #analyse intereactions
    for each in range(len(interestareas)):
        #print("conflict area ", interestareas[each].name, " is in this condition", interestareas[each].status)
        print("The conflict area", interestareas[each].name, "has the following players")
        for each in interestareas:
           print(each.player,"\n")
        #for y in range(interestareas[x].person):
        #    print(interestareas[x].person[y], "has the following options /n")
        
    #increment time 
    world.time =world.time + 1

#######################################################################
#
#ok start program run. create new or load old  game
#
#######################################################################

print ("If you want to start a new game type new, if you want to load an old game type game name "), 
whichgame = input()
#whichgame = "new"
if whichgame in ("new", "New", "NEW","n", "N"):  
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
## add new people, conflicts areas etc
#
######################################################################

print ("The number of objects is ",  world.object_count)

for x in range(0, world.peeps_count):
    peeps[x].sayhi()    
for x in range(0, world.tyrants_count):
    tyrants[x].sayhello()
    tyrants[x].sayhi()	
for x in range(0, world.elected_types_count):
    elected_types[x].sayhowdy()
    elected_types[x].sayhi()

#######################################################################
#add people
#######################################################################

print ("Would you like to create a new person in the world ")
answer = input()
while answer in ("y", "Y", "yes", "Yes", "YES"):
    print ("Enter the name please ",) 
    name = input()
    print ("Select type 1 = person 2 = dictator 3 = elected leader ")
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
    print ("Would you like to create another? ")
    answer = input()

###############################################################################
#add conflict areas
##############################################################################

print ("Create conflict areas, and add players in each area")
answer = "y" 
x = 0
while answer  in ("y", "Y", "yes", "Yes", "YES"):
    name = input ("Enter name of conflict area? ")
    interestareas.append(InterestArea(name))
    interestareas[x].name = name
    answer2 = "y"
    y = 1
    while answer2  in ("y", "Y", "yes", "Yes", "YES"):
        name2 = input ("Enter the name of a person who has interests in this area. ")
        interestareas[x].player.append(name2)
        answer2 = input ("Would you like to add another person? ")
    x += 1
    answer = input ("Would you like to add another conflict area? ")

#######################################################################
#
# ok play game
#
#
########################################################################

print ("Halt here for a minute. Type anything to continue. ")
answer = input()
print ("\n")
print ("Would you like to play the game of world domination? ")
answer =input()
if answer  in ("y", "Y", "yes", "Yes", "YES"):
    run_status = 1
    while run_status == 1:
        gameloop()
        if  input ("Would you like to quit")  in ("y", "Y", "yes", "Yes", "YES"):
            run_status = 0
        pass

########################################################################
#
# save game
#
########################################################################

print ("The number of objects is ", world.object_count)        
print ("Would you like to save the game, y or n ")
answer = input()

if answer in ("no", "n", "No", "NO","N"):
    print ("Thanks for playing see you later gator. ")
elif answer  in ("y", "Y", "yes", "Yes", "YES"):
    print ("What is the name of the file to save? ")
    answer = input ()

    dbfile = open(answer, 'wb')               # use binary mode files in 3.X
    pickle.dump(world, dbfile)
    for x in range (0, world.peeps_count):
        pickle.dump(peeps[x], dbfile)
    for x in range (0, world.tyrants_count):
        pickle.dump(tyrants[x], dbfile)              # data is bytes, not str
    for x in range(0, world. elected_types_count):
        pickle.dump(elected_types[x], dbfile)
    dbfile.close()
    print ("wWe are working on that gator, right now it works... lets see what happens next. ")

print ("Ok see you later.... ")


