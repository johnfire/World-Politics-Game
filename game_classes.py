#!/usr/bin/python3

#####################################################################
#
## classes
#
#####################################################################

class World(object):
    def __init__(self):
        self.name = "the world"
        self.object_count = 0
        self.peeps_count = 0
        self.tyrants_count = 0
        self.elected_types_count = 0
        self.religous_types_cout = 0
        self.time_period = 0  # weekly time period. 01 etc from first year
        self.start_year = 2000

class Person(object):
    def __init__(self,name):
        self.name = name
        self.general_influence = 10
        self.money = 10
        self.personal_power = 10
        self.charisma = 10
        self.popularity = 10
        self.goals = []
        self.strengths = []
        self.weaknesses = []
        self.daring = 5   # 10 is the most, 1 is the least
        self.honesty = 5
        self.abilites = []
        #something for compulsions and constraints... 
        
    def sayhi(self):
        print ("Congrats you have created a instance of a class called person",self.name)
    def increase_value(characteristic):
        characteristic = characteristic + 10
    def increase_value(characteristic):
        characteristic = characteristic - 10

class Dictator(Person):
    def __init__(self,name):
        self.name = name
    def sayhello(self):
        print ("Congrats you have a dictator named ", self.name)

class Elected_Leader(Person):
    def __init__(self,name):
        self.name = name
    def sayhowdy(self):
        print ("congrats you have created a freely elected leader named ",self.name)

class ReligousLeader(Person):
    pass


class Land(object):
    pass
    
class Country(Land):
    def self__init__(self,name):
        self.name = name
        self.energy_resrouces = 0
        self.energy_need = 0
        self.raw_resrouces = 0
        self.raw_need = 0
        self.industrial_resources = 0
        self.industrial_need = 0
        self.population = 0
	

class AreaOfCountry(Land):
    pass
class City(Land):
    pass

class Actions(object):
    pass

class PoliticalInteraction(Actions):
    def __init__(self, first_party, second_party):
        pass
    def theyaretalking(self):
        print ("they are talking")

class War(Actions):
    pass

class Military_Op(Actions):
    pass
