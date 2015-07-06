#!/usr/bin/python3

#####################################################################
#
## classes
#
#####################################################################

class World(object):
    def __init__(self):
        self.name             = "The World"
        self.object_count     = 0
        self.peeps_count      = 0
        self.countries_count  = 0
        self.conflicts_count  = 0
        self.time             = 1  # weekly time period. 01 etc from first year
        self.start_year       = 2000
        self.people           = []
        self.countries        = []
        self.conflictarea     = []

    #################################
    def computeTurn():
        pass

############################################################    
#
############################################################

class Person(object):
    def __init__(self,name):
        self.name               = name
        self.econlevel          = 50
        self.conlevel           = 50
        self.clasper            = []

        self.general_influence  = 10
        self.money              = 10
        self.personal_power     = 10
        self.charisma           = 10
        self.popularity         = 10
        self.daring             = 5   # 10 is the most, 1 is the least
        self.honesty            = 5
        self.goals              = []
        self.strengths          = []
        self.weaknesses         = []
        self.abilites           = []
        
        self.interest_areas     = [] # this is where we keep track of areas of interest, that 
                                     # could and cand conflict with others, ie putin wants ukraine, 
                                     # america doesnt want him in the ukraine. data format is "control of ukraine"

        #something for compulsions and constraints... 
     
    ##########################################   
    def sayhi(self,event):
        print ("Congrats you have created a instance of a class called person",self.name)

    #########################################
    def giveMoney(self,event,amount,person):
        world.person.name.receiveMoney(amount)
        pass

    ##########################################
    def useInfluence(self,event):
        pass

    #########################################
    def useCharisma(self,event):
        pass

    ##########################################
    def useSpecAbility(self,event):
        pass

    #########################################
    def increase_value(self,event, characteristic):
        characteristic = characteristic + 10

    ##########################################
    def increase_value(self,event, characteristic):
        characteristic = characteristic - 10

    #######################################
    def receiveMoney(self,event):
        pass

##################################################################
#
##################################################################

class SpecialAbility():
    def OnInit():
        pass
    
    ########################################
    def controlGovt(self,event):
        Pass
    
    ########################################
    def negotiate(self,event):
        Pass
    
    ########################################
    def startWar(self,event):
        Pass
    
    ########################################
    def spendBusinessMoney(self,event):
        Pass
    
    ########################################
    def spendChurchMoney(self,event):
        Pass
    
    ########################################
    def usePoliticalPressure(self,event):
        Pass
    
    ########################################
    def orderBoycott(self,event):
        Pass
    
    ########################################
    def endBoycott(self,event):
        Pass
    
    ########################################
    def milOperation(self,event):
        Pass
    
    ########################################
    #def (self,event):
        Pass
    
    ########################################
    #def (self,event):
        Pass
    
    ########################################
    #def (self,event):
        Pass
    
    ########################################
    #def (self,event):
        Pass
    
    ########################################
    #def (self,event):
        Pass
    
    ########################################
    #def (self,event):
        Pass
    
    ########################################
    #def (self,event):
        Pass
    
    ########################################
    #def (self,event):
        Pass
    
    ########################################
    #def (self,event):
        Pass
    
    ########################################
    #def (self,event):
        Pass
    
    ########################################
    #def (self,event):
        Pass
    
    ########################################
    #def (self,event):
        Pass



##################################################################
#
###################################################################

class Land(object):
    def self__init__(self,name):
        self.name = name

#################################################################
#
##################################################################
    
class Country(Land):
    def self__init__(self,name):
        self.name                      = name
        self.population                =  0
        self.avgAge                    = 30
        self.ageTilt                   =  0
        self.econcomp                  = 50
        self.soccomp                   = 50
        self.energyNeed                =  0
        self.foodNeed                  =  0
        self.rawResroucesNeed          =  0
        self.militarySize              =  0
        self.militaryResources         =  0
        self.gdp                       =  0
        self.typeOfGovt                =  0
        self.stateOfRebellion          =  0
        self.finishedGoodsProduct      =  0
        self.militaryGoodsProduct      =  0
        self.Debt                      =  0
        #self.       =  0
   
    #######################
    def holdElections(self,event):
        pass
 
    #######################
    def attackCountry(self,event):
        pass

    #######################
    def boycottCountry(self,event):
        pass

    #######################
    def startCivilWar(self,event):
        pass

    #######################
    def sendMoney(self,event):
        pass

    #######################
    def sendOil(self,event):
        pass

    #######################
    def sendRawstuff(self,event):
        pass

    #######################
    def sendFinishedGoods(self,event):
        pass

###################################################################
#
###################################################################	

class AreaOfCountry(Land):
    pass

##################################################################
#
###################################################################

class City(Land):
    pass

###################################################################
#
###################################################################

class Actions(object):
    pass
###################################################################
#
###################################################################

class PoliticalInteraction(Actions):
    def __init__(self, first_party, second_party):
        pass

    ##########################################
    def theyaretalking(self,event):
        print ("they are talking")

###################################################################
#
###################################################################

class War(Actions):
    pass

##################################################################
#
##################################################################

class Military_Op(Actions):
    pass

###################################################################
#
###################################################################

class ConflictArea(object):
    def __init__(self, name):
        self.player            = []
        self.name              = "none"
        self.sort              = "none"
        self.belongsTO         = "a country"
        self.problems          = []
        self.opportunities     = []
        self.activityLevel     = 5

    #######################
    def addPlayers(self,event):
        pass

    #######################
    def attachcountry(self,event):
        pass

    #######################
    def computeOutcome(self,event):
        pass

    #######################
    def sendProducts(self,event):
        pass

    #######################
    def sendOil(self,event):
        pass

    #######################
    def sendRawGoods(self,event):
        pass
