#! /usr/bin/python2.7

#####################
# PURPOSE: A GUI to make Gui's
#
# DATE: 6/6/2013
#
# AUTHOR: Russell Lego
####################

import Tkinter as tk
import ttk
import time
import numpy as np



### Defingin variables for later useage ###

buttonList =[]
checkList  =[]
entryList  =[]

###Defining Functions ####

def getNumber():
    return numerButtonEntry.get()
#def listMaker():
def buttonListMaker(entry):
    buttonText = buttonEntry.get()
    buttonList.append(buttonText)
    buttonEntry.delete(0, tk.END)
    print buttonList

    
def checkMaker():
    checkText = checkboxEntry.get()
    print checkText+'Var=tk.IntVar()'
    print checkText+'Check=tk.Checkbutton(frame, text='+checkText+', variable='+checkText+'Var)'
    checkList.append(checkText)
def entryMaker():
    enrtyText = entryEntry.get()
    print entryText+'Check=tk.Entry(frame, text='+entryText+', variable='+checkText+'Var)'
    entryList.append(entryText)
def guiMaker():
    #opening the main GUI window
    theGuiWindow = tk.Tk()
    guiFrame = tk.Frame(theGuiWindow)
    theGuiWindow.title('''The GUI Window''')
    theGuiWindow.geometry('450x250+500+500')
    #creating all the attributes that we just made using the 'makers'
    for i in range(0, np.size(buttonList)):
        tempLabel = tk.Label(guiFrame, text=buttonList[i])
        tempEntry = tk.Entry(guiFrame)
        tempButton = tk.Button(guiFrame, text=buttonList[i])
        
        tempLabel.grid(row=i, column=0)
        tempEntry.grid(row=i, column=1)
        tempButton.grid(row=i, column=2)
        
    guiFrame.pack()
    theGuiWindow.mainloop()

#######################
# Tk part1   #
#######################


the_window = tk.Tk()
frame = tk.Frame(the_window)
the_window.title('''A GUI for Gui's''')
the_window.geometry('450x250+0+500')
      

ttk.Style().configure('TButton', padding=(0, 5, 0, 5), 
    font='serif 10')
##  ENTRY  ###
buttonLabel = tk.Label(frame, text='Button Name')
buttonLabel.grid(row=0, column=0)
buttonEntry = tk.Entry(frame)
buttonEntry.bind("<Return>", buttonListMaker)
buttonEntry.grid(row=0, column=1)

 


##  BUTTONS  ###
buttonMakerButton = tk.Button(frame, text ='Make Button', command = buttonListMaker)
buttonMakerButton.grid(row=0  , column = 2)

guiMakerButton = tk.Button(frame, text='Make Gui', command=guiMaker)
guiMakerButton.grid(row = 4, column=1)

## packing the window   ###
frame.pack()
the_window.mainloop()  #ONLY FOR WINDOWS USERS