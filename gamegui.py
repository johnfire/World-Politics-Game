#!/usr/bin/python3

#######################################
#
# game gui file: driver for the display windows and app loop
#
#######################################

""" the basic idea is to create a game or simulator that takes real world events and predicts future outcomes based on the data. """

import wx
import os
import os.path
import pickle
from  game_classes1  import World, Person, Land, Country, ConflictArea

######################################

#debug = 1
debug = 0

#######################################
#
# main window of the game
#
#######################################

class MainWindow(wx.Frame):
    def __init__(self, datablock):
        wx.Frame.__init__(self, None, title ="World Domination",  size=(800,600))
        self.panel =wx.Panel(self, -1)
        self.datablk = datablock
        print(self.datablk)
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

        self.newgamebutton     =wx.Button(self,10, label="Start/add data to a new game", pos=(225,50),  size=(350,45),
                                          style =1)
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

        self.Show(True)
    
    ##############################################################

    def NewGame(self,event):
        newGameWindow = NewGameWindow()

    ##############################################################

    def LoadGame(self,event):
        global world
        wildcard = "Python source (*.py)|*.py|" \
        "Compiled Python (*.pyc)|*.pyc|" \
        "All files (*.*)|*.*"
        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.*", style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            # Open the file, read the contents and set them into
            # the text edit window
            filehandle=open(os.path.join(self.dirname, self.filename),'rb')
            datablocke = pickle.load(filehandle)
            world = datablocke
            if debug == 1:
                print("in loop in load game.. ")
                print(datablocke)
                print(world)
                print(world.peeps_count)
                print(world.people)
            filehandle.close()
            # Report on name of latest file read
            #self.SetTitle("Editing ... "+self.filename)
            # Later - could be enhanced to include a "changed" flag whenever
            # the text is actually changed, could also be altered on "save" ...
            dlg.Destroy()

    ##############################################

    def displaygame (self,event):
        #print(self.datablk)
        gamewindow = gameWindow()
        
    #################################################         

    def SaveGame(self,event):
        dlg = wx.FileDialog(None, "Save project as...", os.getcwd(), "", "*.cgg", style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
        inFile = dlg.GetPath()
        if dlg.ShowModal() == wx.ID_OK:
            # Open the file for write, write, close
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            dbfile = open(os.path.join(self.dirname, self.filename), 'ab')    # use binary mode files in 3.X
            pickle.dump(world, dbfile)
            dbfile.close()
            print ("wWe are working on that gator, right now it works... lets see what happens next. ")
            # Get rid of the dialog to keep things tidy
            dlg.Destroy()

    ###########################################
    
    def Settings(self,event):
        settingsWindow = SettingsWindow()
   
    ###########################################

    def ExitGame(self,event): # exit the game
        self.Close(True)
        self.Destroy()

    ##########################################        
    def OnPaint(self,event1):
        pic1 =wx.Bitmap("./fotos/putin.jpg")
        dc = wx.PaintDC(self)
        dc.Clear()
        dc.DrawBitmap(pic1,0,0,True)
        pic2 =wx.Bitmap("./fotos/war.jpg")
        dc.DrawBitmap(pic2,400,0,True)
        pic3 =wx.Bitmap("./fotos/angela.jpg")
        dc.DrawBitmap(pic3, 400, 380,True)
        
    ########################################    
           
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
    def __init__(self):
        wx.Frame.__init__(self, None, title ="World Domination: New Game",  size=(600,400))
        self.createPerson       =wx.Button(self,20,label="Create a person",       pos=(225,50 ),size=(350,45),style=1)
        self.createLand         =wx.Button(self,21,label="Create a place",        pos=(225,100),size=(350,45),style=1)
        self.createConflictArea =wx.Button(self,22,label="Create a conflict area",pos=(225,150),size=(350,45),style=1)
        self.createNext         =wx.Button(self,24,label="Create blank",          pos=(225,200),size=(350,45),style=1)
        self.quitbutton         =wx.Button(self,23,label="Finished creating",     pos=(225,250),size=(350,45),style=1)

        self.Bind(wx.EVT_BUTTON, self.makeperson,       self.createPerson)
        self.Bind(wx.EVT_BUTTON, self.makeland,         self.createLand)
        self.Bind(wx.EVT_BUTTON, self.makeconflictarea, self.createConflictArea)
        self.Bind(wx.EVT_BUTTON, self.makenext,         self.createNext)
        self.Bind(wx.EVT_BUTTON, self.ExitScreen,       self.quitbutton)
     
        self.Show()

    ##########################################

    def makeperson(self,event):
        makepeople = MakePerson()

    #########################################

    def makeland(self, event):
        makecountry =MakeCountry()

    #########################################

    def makeconflictarea(self,event):
        makeconflict = MakeConflict()
    
    ########################################

    def makenext(self,event):
        pass

    ########################################

    def ExitScreen(self,event):
        self.Close(True)

################################################################
################################################################

class SettingsWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title ="World Domination: Settings",  size=(600,400))
        pass
        self.Show()

##################################################################
class gameWindow(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title ="World Domination: Game Status",  size=(600,500))
        self.panel =wx.Panel(self,-1)
        self.tree = wx.TreeCtrl(self.panel,pos=(20,20),size=(150,299))
        theworld  = self.tree.AddRoot("People")
        if debug == 1:
            for x in range(0,len(world.people)):
                print(x)
                print(world.people[x])
        for y in range(0, len(world.people)):
            self.tree.AppendItem(theworld, world.people[y].name)

        self.treecntry = wx.TreeCtrl(self.panel,pos=(180,20),size=(150,299))
        the_countries  = self.treecntry.AddRoot("Countries")
        
        if len(world.countries) > 0:
            for x in range(0, len(world.countries)):
                self.treecntry.AppendItem(the_countries, world.countries[x].name)

        self.treeconflict = wx.TreeCtrl(self.panel,pos=(340,20),size=(150,299))
        theconflicts  = self.treeconflict.AddRoot("Conflicts")
        
        if len(world.conflictarea) > 0:
            for x in range(0, len(world.conflictarea)):
                self.treeconflict.AppendItem(theconflicts, world.conflictarea[x].name)
        
        closebutton =wx.Button(self.panel,-1,"close",pos=(25,320),size=(250,50))

        self.Bind(wx.EVT_BUTTON, self.closewindow, closebutton)

        self.Show()

    #######################################################

    def closewindow (self,event):
        self.Close(True)
           

####################################################################
#
# make new people, places events etc 
#
#################################################################


class MakePerson(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title ="World Domination: Create a new Country",  size=(800,700))
        self.panel = wx.Panel(self,-1)
        self.panel.SetBackgroundColour('white')
        text1 =wx.StaticText(self.panel, -1, "Name of Person",                pos=(20,20))
        text2 =wx.StaticText(self.panel, -1, "Economic Compass",              pos=(20,80))
        text3 =wx.StaticText(self.panel, -1, "Social Compass  ",              pos=(20,140))
        text4 =wx.StaticText(self.panel, -1, "General influence -100 to 100", pos=(20,200))
        text5 =wx.StaticText(self.panel, -1, "Money (thousands of euros)",    pos=(20,240))
        text6 =wx.StaticText(self.panel, -1, "Personal Power -100 to 100",    pos=(20,280))
        text7 =wx.StaticText(self.panel, -1, "Charisma -10 to 10",            pos=(20,320))
        text8 =wx.StaticText(self.panel, -1, "Popularity -100 to 100",        pos=(20,360))
        text9 =wx.StaticText(self.panel, -1, "Daring -10 to 10",              pos=(20,400))
        text10=wx.StaticText(self.panel, -1, "Honesty-10 to 10",              pos=(20,440))
        text11=wx.StaticText(self.panel, -1, "Goals",                         pos=(20,480))
        text12=wx.StaticText(self.panel, -1, "Strengths",                     pos=(20,520))
        text13=wx.StaticText(self.panel, -1, "Weaknesses",            pos=(470,200))
        text14=wx.StaticText(self.panel, -1, "Wants",                 pos=(470,240))
        text15=wx.StaticText(self.panel, -1, "open",                  pos=(470,280))
        text16=wx.StaticText(self.panel, -1, "open",                  pos=(470,320))
        text17=wx.StaticText(self.panel, -1, "open", pos=(470,360))
        text18=wx.StaticText(self.panel, -1, "open", pos=(470,400))
        text19=wx.StaticText(self.panel, -1, "open", pos=(470,440))
        text20=wx.StaticText(self.panel, -1, "open", pos=(470,480))
  
        ### entry boxes etc....

        self.name       =wx.TextCtrl(self.panel, -1, " ", pos=(200,20),size=(200,-1))

        self.econslider =wx.Slider(self.panel, -1, 0, -100,100, pos=(200,60), size =(370,-1),
                                   style=(wx.SL_AUTOTICKS | wx.SL_LABELS ))
        self.econslider.SetTickFreq(1)
        self.socslider  =wx.Slider(self.panel, -1, 0, -100,100, pos=(200,120), size =(370,-1),
                                   style=(wx.SL_AUTOTICKS | wx.SL_LABELS ))
        self.socslider.SetTickFreq(1)
        
        self.influence      =wx.TextCtrl(self.panel, -1, " ", pos=(300,200),size=(100,-1))
        self.money          =wx.TextCtrl(self.panel, -1, " ", pos=(300,240),size=(100,-1))
        self.power          =wx.TextCtrl(self.panel, -1, " ", pos=(300,280),size=(100,-1))
        self.charisma       =wx.TextCtrl(self.panel, -1, " ", pos=(300,320),size=(100,-1))
        self.popularity     =wx.TextCtrl(self.panel, -1, " ", pos=(300,360),size=(100,-1))
        self.daring         =wx.TextCtrl(self.panel, -1, " ", pos=(300,400),size=(100,-1)) 
        self.honesty        =wx.TextCtrl(self.panel, -1, " ", pos=(300,440),size=(100,-1))






        self.name.SetInsertionPoint(0)

        savebutton =wx.Button(self.panel,-1,"Save data",pos=(100,610))
        exitbutton =wx.Button(self.panel,-1,"Exit people creation",pos=(350,610))
        self.Bind(wx.EVT_BUTTON, self.savedata, savebutton)
        self.Bind(wx.EVT_BUTTON, self.exitscr, exitbutton)

        self.Show()

    ############################################
    
    def savedata(self,event):
        tempdata = Person(self.name.GetValue())
        #tempdata.name = self.name.GetValue()
        tempdata.econcomp = self.econslider.GetValue() 
        tempdata.soccomp = self.socslider.GetValue()
        tempdata.clasper = "regular guy"

        if debug == 1:
            print(tempdata)
            print(tempdata.name)
            print(tempdata.econcomp)
            print(tempdata.soccomp)

        world.people.append(tempdata)
        
        world.object_count += 1
        world.peeps_count += 1

    #####################################

    def exitscr(self,event):
        self.Close(True)


################################################################
#
#make country
#
#################################################################

class MakeCountry(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title ="World Domination: Create a new Country",  size=(800,700))
        self.panel = wx.Panel(self,-1)
        self.panel.SetBackgroundColour('blue')
        text1 =wx.StaticText(self.panel, -1, "Name of Country",             pos=(20,20))
        text2 =wx.StaticText(self.panel, -1, "Economic level",              pos=(20,80))
        text3 =wx.StaticText(self.panel, -1, "Social orientation ",         pos=(20,140))
        text4 =wx.StaticText(self.panel, -1, "Population",                  pos=(20,180))
        text5 =wx.StaticText(self.panel, -1, "GDP",                         pos=(20,220))
        text6 =wx.StaticText(self.panel, -1, "growth rate",                 pos=(20,260))
        text7 =wx.StaticText(self.panel, -1, "ag self sufficency",          pos=(20,300))
        text8 =wx.StaticText(self.panel, -1, "average age",                 pos=(20,360))
        text9 =wx.StaticText(self.panel, -1, "young med or old",            pos=(20,400))
        text10=wx.StaticText(self.panel, -1, "oil need or surplus",         pos=(20,440))
        text11=wx.StaticText(self.panel, -1, "food  need or surplus",       pos=(20,480))
        text12=wx.StaticText(self.panel, -1, "Raw goods  need or surplus",  pos=(20,520))
        text13=wx.StaticText(self.panel, -1, "finished goods  need or surplus",   pos=(470,200))
        text14=wx.StaticText(self.panel, -1, "Military Size",               pos=(470,240))
        text15=wx.StaticText(self.panel, -1, "military ability 1 to 10",    pos=(470,280))
        text16=wx.StaticText(self.panel, -1, "GDP",                         pos=(470,320))
        text17=wx.StaticText(self.panel, -1, "type of govt",                pos=(470,360))
        text18=wx.StaticText(self.panel, -1, "stability",                   pos=(470,400))
        text19=wx.StaticText(self.panel, -1, "debt",                        pos=(470,440))
        text20=wx.StaticText(self.panel, -1, "military production",         pos=(470,480))

        self.name =wx.TextCtrl(self.panel, -1, " ", pos=(200,20),size=(200,-1))
        self.econslider =wx.Slider(self.panel, -1, 50, 0, 100, pos=(200,60), size =(370,-1),
                                   style=(wx.SL_AUTOTICKS | wx.SL_LABELS ))
        self.econslider.SetTickFreq(1)
        self.socslider  =wx.Slider(self.panel, -1, 0, -100, 100, pos=(200,120),size =(370,-1),
                                   style=(wx.SL_AUTOTICKS | wx.SL_LABELS ))
        self.socslider.SetTickFreq(1)
        


        self.name.SetInsertionPoint(0)
        savebutton =wx.Button(self.panel, -1, "save data",             pos=(100,600))
        exitbutton =wx.Button(self.panel, -1, "Exit country creation", pos=(350,600))
        self.Bind(wx.EVT_BUTTON, self.savedata, savebutton)
        self.Bind(wx.EVT_BUTTON, self.exitscr, exitbutton)
        self.Show()

    ##############################################
    
    def savedata(self,event):
        tempdata = Country()
        tempdata.name = self.name.GetValue()
        tempdata.econcomp = self.econslider.GetValue() 
        tempdata.soccomp = self.socslider.GetValue()
        
        if debug == 1:
            print(tempdata)
            print(tempdata.name)
            print(tempdata.econcomp)
            print(tempdata.soccomp)
        world.countries.append(tempdata)
        world.object_count += 1
        world.countries_count += 1
        
        if debug == 1:
            countryname =self.name.GetValue()
            print(countryname)
            econlevel =self.econslider.GetValue()
            print(econlevel)

    ###########################################

    def exitscr(self,event):
        self.Close(True)


################################################################
#
#                make conflict area
#
###############################################################


class MakeConflict(wx.Frame):
    def __init__(self):
        print("i am in the conflict init routine")
        wx.Frame.__init__(self, None, title ="World Domination: Create a new conflict area",  size=(590,450))
        self.panel = wx.Panel(self,-1)
        self.panel.SetBackgroundColour('pink')
        text1 =wx.StaticText(self.panel, -1, "Name of area", pos=(20,20))
        text2 =wx.StaticText(self.panel, -1, "Players",              pos=(20,80))
        text3 =wx.StaticText(self.panel, -1, "Belongs to",         pos=(20,140))
        text4 =wx.StaticText(self.panel, -1, "Problems",                  pos=(20,180))
        text5 =wx.StaticText(self.panel, -1, "Opportunities",                         pos=(20,220))
        text6 =wx.StaticText(self.panel, -1, "activity level",                 pos=(20,260))
        text7 =wx.StaticText(self.panel, -1, "a",          pos=(20,300))
        text8 =wx.StaticText(self.panel, -1, "a",                 pos=(20,360))
        text9 =wx.StaticText(self.panel, -1, "y",            pos=(20,400))
        text10=wx.StaticText(self.panel, -1, "o",         pos=(20,440))
        text11=wx.StaticText(self.panel, -1, "f",       pos=(20,480))
        text12=wx.StaticText(self.panel, -1, "R",  pos=(20,520))
        text13=wx.StaticText(self.panel, -1, "f",   pos=(470,200))
        text14=wx.StaticText(self.panel, -1, "m",               pos=(470,240))
        text15=wx.StaticText(self.panel, -1, "m",    pos=(470,280))
        text16=wx.StaticText(self.panel, -1, "G",                         pos=(470,320))
        text17=wx.StaticText(self.panel, -1, "j",                pos=(470,360))
        text18=wx.StaticText(self.panel, -1, "s",                   pos=(470,400))
        text19=wx.StaticText(self.panel, -1, "d",                        pos=(470,440))
        text20=wx.StaticText(self.panel, -1, "m",         pos=(470,480))


        self.name =wx.TextCtrl(self.panel, -1, " ", pos=(200,20), size=(200,-1))
        savebutton =wx.Button(self.panel, -1, "Save data",              pos=(100,340))
        exitbutton =wx.Button(self.panel, -1, "Exit conflict creation", pos=(350,340))
        self.Bind(wx.EVT_BUTTON, self.savedata, savebutton)
        self.Bind(wx.EVT_BUTTON, self.exitscr, exitbutton)
        self.Show()
    
    #################################################

    def savedata(self,event):
        tempdata = Country()
        tempdata.name = self.name.GetValue()
        if debug == 1:
            print(tempdata)
            print(tempdata.name)
        world.conflictarea.append(tempdata)
        world.object_count += 1
        world.conflicts_count += 1
        
        if debug == 1:
            countryname =self.name.GetValue()
            print(countryname)


    ##########################

    def exitscr(self,event):
        self.Close(True)


####################################################################
#
#                           RUN THE APP
#
###################################################################       

app = wx.App()
world = World()

if debug == 1:
    print(world)

frame = MainWindow(world)
app.MainLoop()


