#!/usr/bin/python3

#####################################################################
#
## classes
#
#####################################################################

class World(object):
    def __init__(self):
        self.name = "The World"
        self.object_count = 0
        self.peeps_count = 0
        self.countries_count = 0
        self.conflicts_count = 0
        self.time = 1  # weekly time period. 01 etc from first year
        self.start_year = 2000
        self.people = []
        self.countries = []
        self.conflictarea = []


############################################################

class Person(object):
    def __init__(self,name):
        self.name = name
        self.econlevel = 50
        self.conlevel = 50
        self.clasper = []

        self.general_influence = 10
        self.money = 10
        self.personal_power = 10
        self.charisma = 10
        self.popularity = 10
        self.daring = 5   # 10 is the most, 1 is the least
        self.honesty = 5
        self.goals = []
        self.strengths = []
        self.weaknesses = []
        self.abilites = []
        
        self.interest_areas = [] # this is where we keep track of areas of interest, that could and cand conflict with others, ie putin wants ukraine, america doesnt want him in the ukraine. data format is "control of ukraine"

        #something for compulsions and constraints... 
        
    def sayhi(self):
        print ("Congrats you have created a instance of a class called person",self.name)

    def increase_value(characteristic):
        characteristic = characteristic + 10

    def increase_value(characteristic):
        characteristic = characteristic - 10

###################################################################
class Land(object):
    def self__init__(self,name):
        self.name = name
##################################################################
    
class Country(Land):
    def self__init__(self,name):
        self.name = name
        self.econcomp = 50
        self.soccomp =50
        self.energy_resrouces = 0
        self.energy_need = 0
        self.raw_resrouces = 0
        self.raw_need = 0
        self.industrial_resources = 0
        self.industrial_need = 0
        self.population = 0

###################################################################	

class AreaOfCountry(Land):
    pass

###################################################################

class City(Land):
    pass

###################################################################

class Actions(object):
    pass

###################################################################

class PoliticalInteraction(Actions):
    def __init__(self, first_party, second_party):
        pass
    def theyaretalking(self):
        print ("they are talking")

###################################################################

class War(Actions):
    pass

##################################################################

class Military_Op(Actions):
    pass

###################################################################

class ConflictArea(object):
    def __init__(self, name):
        self.player = []
        self.name = "none"
        self.sort = "none"

