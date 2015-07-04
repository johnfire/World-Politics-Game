#!/usr/bin/python3

#######################################
#
# game gui file
#
#######################################

import wx
import os
import os.path
import pickle
from  game_classes1  import *

######################################
#######################################
#
# psuedo global variables.
#
######################################

testinput ="   "
#human agents in the game

peeps = []

#countries, areas cities etc

#countries = []
#areas = []
#cities = []
#towns = []
#oceans = []
#seas = []

#government, non government organizations etc

#governments = []
#ngos = []
#interest_groups = []
#companies = []

#actions by human agents in game

actions = []

#conflict area list

conflicts =[]

world = World()
peepscount=0
#######################################
#
# main window of the game
#
#######################################

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title ="World Domination",  size=(800,600))
        self.panel =wxPanel(self, -1)
        filemenu = wx.Menu()
        helpmenu = wx.Menu()
        ################################
        menuNew  = filemenu.Append(wx.ID_NEW, "N&ew game")
        menuOld  = filemenu.Append(wx.ID_OPEN,"O&pen saved game")
        menuSave = filemenu.Append(wx.ID_SAVE,"S&ave current game")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT,"Q&uit")
        ################################
        menuHelp = helpmenu.Append(wx.ID_HELP,"H&elp")
        menuSet  = helpmenu.Append(6,"Settings")
        helpmenu.AppendSeparator()
        menuAbout = helpmenu.Append(wx.ID_ABOUT,"A&bout")
        ################################
        menuBar=wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        menuBar.Append(helpmenu,"&Help")
        menuBar.SetBackgroundColour('White')
        ###################################


        self.Bind(wx.EVT_MENU, self.ExitGame, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout,  menuAbout)
        self.Bind(wx.EVT_MENU, self.LoadGame, menuOld)
        #self.Bind(wx.EVT_MENU, self.displaygame, self.currentgamebut)
        self.Bind(wx.EVT_MENU, self.SaveGame, menuSave)

        self.SetMenuBar(menuBar)
        self.CreateStatusBar() # A StatusBar in the bottom of the window
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.newgamebutton     =wx.Button(self,10, label="Start a new game", pos=(225,50),  size=(350,45),style =1)
        self.oldgamebutton     =wx.Button(self,11, label="Load a prev game", pos=(225,100), size=(350,45),style =1)
        self.currentgamebutton =wx.Button(self,15, label="show current game",pos=(225,150), size=(350,45),style=1)
        self.savebutton        =wx.Button(self,12, label="Save current game",pos=(225,200), size=(350,45), style =1)
        self.settingbutton     =wx.Button(self,13, label="Settings",         pos=(225,250), size=(350,45), style =1)
        self.quitbutton        =wx.Button(self,14, label="End Game",         pos=(225,300), size=(350,45),style=1)

        self.Bind(wx.EVT_BUTTON, self.NewGame,  self.newgamebutton)
        self.Bind(wx.EVT_BUTTON, self.LoadGame, self.oldgamebutton)
        self.Bind(wx.EVT_BUTTON, self.displaygame, self.currentgamebutton)
        self.Bind(wx.EVT_BUTTON, self.SaveGame, self.savebutton)
        self.Bind(wx.EVT_BUTTON, self.Settings, self.settingbutton)
        self.Bind(wx.EVT_BUTTON, self.ExitGame, self.quitbutton)
        self.SetBackgroundColour('red')
       
        #peeps.append(Person("Chris"))
        #world.object_count += 1
        #world.peeps_count += 1
        self.Show(True)
    
    ##############################################################

    def NewGame(self,event):
        newGameWindow = NewGameWindow(None,"im here")

    ##############################################################

    def LoadGame(self,event):
        wildcard = "Python source (*.py)|*.py|" \
        "Compiled Python (*.pyc)|*.pyc|" \
        "All files (*.*)|*.*"
        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.*", style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            self.control=[]
            # Open the file, read the contents and set them into
            # the text edit window
            filehandle=open(os.path.join(self.dirname, self.filename),'rb')
            world = pickle.load(filehandle)
            print(world.peeps_count)
            peepscount = world.peeps_count
            print(peepscount)
            for x in range(0, world.peeps_count):
                peeps.append(pickle.load(filehandle))
                print(peeps[x].name)
            for y in range(0, world.countries_count):
                countries.append(pickle.load(filehandle))
                print(countries[y].name)
            for z in range(0, world.conflicts_count):
                conflicts.append(pickle.load(filehandle))
                print(conflicts[z].name)
            filehandle.close()
            # Report on name of latest file read
            self.SetTitle("Editing ... "+self.filename)
            # Later - could be enhanced to include a "changed" flag whenever
            # the text is actually changed, could also be altered on "save" ...
            dlg.Destroy()

    def displaygame (self,event):
        gamewindow = gameWindow(None,"blahblah")
        
         

    def SaveGame(self,event):
        dlg = wx.FileDialog(None, "Save project as...", os.getcwd(), "", "*.cgg", style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
        inFile = dlg.GetPath()
        if dlg.ShowModal() == wx.ID_OK:
            # Open the file for write, write, close
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            dbfile = open(os.path.join(self.dirname, self.filename), 'ab')    # use binary mode files in 3.X
            pickle.dump(world, dbfile)
            for x in range (0, world.peeps_count):
                pickle.dump(peeps[x], dbfile)
            for y in range (0, world.countries_count):
                pickle.dump(countries[y], dbfile)
            for z in range (0, world.conflicts_count):
                pickle.dump(conflicts[z], dbfile)
            dbfile.close()
            print ("wWe are working on that gator, right now it works... lets see what happens next. ")
            # Get rid of the dialog to keep things tidy
            dlg.Destroy()
    
    def Settings(self,event):
        settingsWindow = SettingsWindow(None,"blahblah")

    def ExitGame(self,event): # exit the game
        self.Close(True)
        self.Destroy()
        
    def OnPaint(self,event1):
        pic1 =wx.Bitmap("putin.jpg")
        dc = wx.PaintDC(self)
        dc.Clear()
        dc.DrawBitmap(pic1,0,0,True)
        pic2 =wx.Bitmap("war.jpg")
        dc.DrawBitmap(pic2,400,0,True)
        pic3 =wx.Bitmap("angela.jpg")
        dc.DrawBitmap(pic3, 400, 380,True)
           
    def OnAbout(self,event):
         # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "A game to simulate world politics \nBy Chris Rehm\nCurrently licenced under the creative commons licence\nCreated June 2015, Linden Germany", " About World Domination", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.


###################################################
#
# new game window stuff
#
###################################################

class NewGameWindow(wx.Frame):
    def __init__(self,parent, title):
        wx.Frame.__init__(self, parent, title ="World Domination: New Game",  size=(600,400))
        self.createPerson       =wx.Button(self,20, label="Create a person",pos=(225,50), size=(350,45),style =1)
        self.createLand         =wx.Button(self,21, label="Create a place",pos=(225,100), size=(350,45),style =1)
        self.createConflictArea =wx.Button(self,22, label="Create a conflict area",pos=(225,150),size=(350,45), style =1)
        self.createNext         =wx.Button(self,22, label="Create blank", pos=(225,200),size=(350,45), style =1)
        self.quitbutton         =wx.Button(self,23, label="Finished creating", pos=(225,250),size=(350,45),style=1)

        self.Bind(wx.EVT_BUTTON, self.makeperson,       self.createPerson)
        self.Bind(wx.EVT_BUTTON, self.makeland,         self.createLand)
        self.Bind(wx.EVT_BUTTON, self.makeconflictarea, self.createConflictArea)
        self.Bind(wx.EVT_BUTTON, self.makenext,         self.createNext)
        self.Bind(wx.EVT_BUTTON, self.ExitScreen,       self.quitbutton)
     
        self.Show()

    def makeperson(self,event):
        makepeople = MakePerson(self, "AAA")

    def makeland(self, event):
        makecountry =MakeCountry(self, "BBB")

    def makeconflictarea(self,event):
        makeconflict =MakeConflict(self,"XXX")

    def makenext(self,event):
        pass

    def ExitScreen(self,event):
        self.Close(True)


#############################################################

################################################################


class SettingsWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title ="World Domination: Settings",  size=(600,400))
        self.Show()

##################################################################
class gameWindow(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title ="World Domination: Game Status",  size=(600,500))
        panel =wx.Panel(self,-1)

        self.tree = wx.TreeCtrl(panel,pos=(20,20),size=(150,299))
        theworld  = self.tree.AddRoot("People")
        #print(peepscount)#
        for x in range(0,len(peeps)):
            #print(x)
            #print(peeps)
            self.tree.AppendItem(theworld, peeps[x].name)

        self.treecntry = wx.TreeCtrl(panel,pos=(180,20),size=(150,299))
        the_countries  = self.treecntry.AddRoot("Countries")
        for x in range(0, len(countries)):
           self.treecntry.AppendItem(the_countries, countries[x].name)

        self.treeconflict = wx.TreeCtrl(panel,pos=(340,20),size=(150,299))
        theconflicts  = self.treeconflict.AddRoot("conflicts")
        for x in range(0, len(conflicts)):
            self.treeconflict.AppendItem(theconflicts, conflicts[x].name)
        
        closebutton =wx.Button(panel,-1,"close",pos=(25,320),size=(250,50))
        self.Bind(wx.EVT_BUTTON, self.closewindow, closebutton)

        self.Show()

    def closewindow (self,event):
        self.Close(True)
           

####################################################################
#
# make new people, places events etc 
#
#################################################################


class MakePerson(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title ="World Domination: Create a new Country",  size=(590,390))
        panel = wx.Panel(self,-1)
        panel.SetBackgroundColour('white')
        text1 =wx.StaticText(panel, -1, "Name of Person", pos=(20,20))
        text2 =wx.StaticText(panel, -1, "Economic Compass", pos=(20,80))
        text3 =wx.StaticText(panel, -1, "Social Compass  ", pos=(20,140))

        self.name =wx.TextCtrl(panel, -1, " ", pos=(200,20),size=(200,-1))

        self.econslider =wx.Slider(panel,-1,0,-100,100, pos=(200,60),size =(370,-1),style=(wx.SL_AUTOTICKS | wx.SL_LABELS ))
        self.econslider.SetTickFreq(1)
        self.socslider  =wx.Slider(panel,-1,0,-100,100, pos=(200,120),size =(370,-1),style=(wx.SL_AUTOTICKS | wx.SL_LABELS ))
        self.socslider.SetTickFreq(1)
        
        self.name.SetInsertionPoint(0)

        savebutton =wx.Button(panel,-1,"Save data",pos=(100,300))
        exitbutton =wx.Button(panel,-1,"Exit people creation",pos=(350,300))
        self.Bind(wx.EVT_BUTTON, self.savedata, savebutton)
        self.Bind(wx.EVT_BUTTON, self.exitscr, exitbutton)

        self.Show()
    
    def savedata(self,event):
        tempdata = Person(self.name)
        tempdata.name = self.name.GetValue()
        tempdata.econcomp = self.econslider.GetValue() 
        tempdata.soccomp = self.socslider.GetValue()
        tempdata.clasper = "regular guy"
        #print(tempdata)
        print(tempdata.name)
        print(tempdata.econcomp)
        print(tempdata.soccomp)
        peeps.append(tempdata)
        world.object_count += 1
        world.peeps_count += 1

    def exitscr(self,event):
        self.Close(True)


################################################################
#
#make country
#
#################################################################

class MakeCountry(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title ="World Domination: Create a new Country",  size=(590,450))
        panel = wx.Panel(self,-1)
        #panel.SetBackgroundColour('white')
        text1 =wx.StaticText(panel, -1, "Name of Country", pos=(20,20))
        text2 =wx.StaticText(panel, -1, "Economic level", pos=(20,80))
        text3 =wx.StaticText(panel, -1, "Social orientation ", pos=(20,140))
        text4 =wx.StaticText(panel, -1, "Population", pos=(20,180))
        text5 =wx.StaticText(panel, -1, "GDP", pos=(20,220))
        text6 =wx.StaticText(panel, -1, "growth rate", pos=(20,260))
        text7 =wx.StaticText(panel, -1, "ag self sufficency", pos=(20,300))

        self.name =wx.TextCtrl(panel, -1, " ", pos=(200,20),size=(200,-1))
        self.econslider =wx.Slider(panel,-1,50, 0,100, pos=(200,60),size =(370,-1),
                                   style=(wx.SL_AUTOTICKS | wx.SL_LABELS ))
        self.econslider.SetTickFreq(1)
        self.socslider  =wx.Slider(panel,-1,0,-100,100, pos=(200,120),size =(370,-1),
                                   style=(wx.SL_AUTOTICKS | wx.SL_LABELS ))
        self.socslider.SetTickFreq(1)
        
        self.name.SetInsertionPoint(0)
        savebutton =wx.Button(panel,-1,"save data",pos=(100,340))
        exitbutton =wx.Button(panel,-1,"Exit country creation",pos=(350,340))
        self.Bind(wx.EVT_BUTTON, self.savedata, savebutton)
        self.Bind(wx.EVT_BUTTON, self.exitscr, exitbutton)
        self.Show()
    
    def savedata(self,event):
        tempdata = Country()
        tempdata.name = self.name.GetValue()
        tempdata.econcomp = self.econslider.GetValue() 
        tempdata.soccomp = self.socslider.GetValue()
        #tempdata.clasper = "regular guy"
        #print(tempdata)
        print(tempdata.name)
        print(tempdata.econcomp)
        print(tempdata.soccomp)
        countries.append(tempdata)
        world.object_count += 1
        world.countries_count += 1
        
        countryname =self.name.GetValue()
        print(countryname)
        econlevel =self.econslider.GetValue()
        print(econlevel)
        soc =self.socslider.GetValue()
        print(soc)

    def exitscr(self,event):
        self.Close(True)


################################################################
#
#                make conflict area
#
###############################################################


class MakeConflict(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title ="World Domination: Create a new conflict area",  size=(590,450))
        panel = wx.Panel(self,-1)
        #panel.SetBackgroundColour('white')
        text1 =wx.StaticText(panel, -1, "Name of area", pos=(20,20))

        self.name =wx.TextCtrl(panel, -1, " ", pos=(200,20),size=(200,-1))

        self.econslider =wx.Slider(panel,-1,50, 0,100, pos=(200,60),size =(370,-1),
                                   style=(wx.SL_AUTOTICKS | wx.SL_LABELS ))
        self.econslider.SetTickFreq(1)

        self.socslider  =wx.Slider(panel,-1,0,-100,100, pos=(200,120),size =(370,-1),
                                   style=(wx.SL_AUTOTICKS | wx.SL_LABELS ))
        self.socslider.SetTickFreq(1)
        
        self.name.SetInsertionPoint(0)
        savebutton =wx.Button(panel,-1,"save data",pos=(100,340))
        exitbutton =wx.Button(panel,-1,"Exit conflict creation",pos=(350,340))
        self.Bind(wx.EVT_BUTTON, self.savedata, savebutton)
        self.Bind(wx.EVT_BUTTON, self.exitscr, exitbutton)
        self.Show()
    
    def savedata(self,event):
        tempdata = Countries(self.name)
        tempdata.name = self.name.GetValue()
        #tempdata.econcomp = self.econslider.GetValue() 
        #tempdata.soccomp = self.socslider.GetValue()
        #tempdata.clasper = "regular guy"
        #print(tempdata)
        print(tempdata.name)
        print(tempdata.econcomp)
        print(tempdata.soccomp)
        peeps.append(tempdata)
        world.object_count += 1
        world.countries_count += 1
        
        countryname =self.name.GetValue()
        print(countryname)
        econlevel =self.econslider.GetValue()
        print(econlevel)
        soc =self.socslider.GetValue()
        print(soc)

    def exitscr(self,event):
        self.Close(True)


####################################################################
#
#                           RUN THE APP
#
###################################################################       

app = wx.App(False)
frame = MainWindow(None, "World Domination")
app.MainLoop()


