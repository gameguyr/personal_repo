#! /usr/bin/python2.7

#####################
# PURPOSE:to test checkboxes in tkinter package
#
# DATE:6/5/2013
#
# AUTHOR: Russell Lego
####################

import gdata
import gdata.youtube
import gdata.youtube.service
import Tkinter as tk
import tkMessageBox as mb
from Tkinter import Tk, W, E
from ttk import Frame, Button, Label, Style
from ttk import Entry
import time


def testCheck():
    if timeVar.get() == 1:
        print 'Checked'
def PrintOption():
    print variable.get()

#######################
# Tk part   #
#######################


the_window = tk.Tk()
frame = Frame(the_window)
      

Style().configure('TButton', padding=(0, 5, 0, 5), 
    font='serif 10')


##  ENTRY  ###

timeVar = tk.IntVar()
timeCheck = tk.Checkbutton(frame, text='Search by Time', variable=timeVar)
timeCheck.grid(row=1, column=2)



##  BUTTONS  ###
searchButton = Button(frame, text ='Search', command = testCheck)
searchButton.grid(row=2  , column = 2)

searchButton = Button(frame, text ='Print Option', command = PrintOption)
searchButton.grid(row=3  , column = 2)

##  Menu ###
variable = tk.StringVar()
variable.set("one") # default value

w = tk.OptionMenu(frame, variable, "one", "two", "three")
w.grid(row=4  , column = 2)



frame.pack()
the_window.mainloop()