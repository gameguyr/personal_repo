#! /usr/bin/python2.7

#####################
# PURPOSE: to visualize any structure from the SDSS
#
# DATE: 6/26/2013
#
# AUTHOR: Russell Lego
####################


import pyfits as pf
import matplotlib.pylab as plt
import numpy as np
import Tkinter as tk
import tkMessageBox as mb


#filePath = '/Users/rlego/Dropbox/PythonWorkspace/lowzPython/lowz.fits'

#filePath = '/Users/rlego/Dropbox/final_search/fin_cat.fits'
#catList = pf.open(filePath)

#catData = catList[1].data

c = 3.0E5
h = 100.0

def LoadCatalog():
    global catData
    filePath = CatalogEntry.get()
    catList = pf.open(filePath)
    catData = catList[1].data
    print '''
    Catalog Loaded
    
    '''
    
    
def bandSelector(band):
    if band=='u':
        bandMag=catData.field('MODELMAG_U')
    if band=='g':
        bandMag=catData.field('modelmag_g')
    if band=='r':
        bandMag=catData.field('modelmag_r')
    if band=='i':
        bandMag=catData.field('modelmag_i')
    if band=='z':
        bandMag=catData.field('modelmag_z')
    if band=='j':
        bandMag=catData.field('modelmag_j')
    if band=='h':
        bandMag=catData.field('modelmag_h')
    if band=='k':
        bandMag=catData.field('modelmag_k')
    return bandMag

    
def sizeMag():
#    catData = LoadCatalog(CatalogEntry.get())
    bandMag = bandSelector(band1Entry.get())
    r50 = np.dot(catData.field('PETROTH50'), 1/float(206265))
    distance = np.dot(catData.field('Z'), (c/h)*1E6)
    size = np.dot(r50, distance)
    plt.scatter(bandMag, np.log10(size),  marker='.', s=0.1)
    plt.ylabel('Half Light Radius [Parsecs]')
    plt.xlabel('Absolute Magnitude')
    plt.title('Size Magnitude Diagram')
    plt.xlim((-23, -12))
    plt.ylim((-3.25, -1.25))
    return plt.show()

def HR():
#    catData = LoadCatalog(CatalogEntry.get())
    bandMag = bandSelector(band1Entry.get())
    otherBandMag = bandSelector(band2Entry.get())
    plt.scatter(np.subtract(bandMag, otherBandMag), bandMag,  marker='.', s=0.1)
    plt.ylabel('Absolute Magnitude   '+band1Entry.get()+' Band')
    plt.xlabel(band1Entry.get()+' - '+band2Entry.get())
    plt.title('H-R Diagram')
    plt.xlim((-0.25, 1.25))
    plt.ylim((-23, -11))
    return plt.show()

def colorColor():
#    catData = LoadCatalog(CatalogEntry.get())
    bandMag = bandSelector(band1Entry.get())
    otherBandMag = bandSelector(band2Entry.get())
    bandMag2 = bandSelector(band3Entry.get())
    otherBandMag2 = bandSelector(band4Entry.get())
    plt.scatter(np.subtract(bandMag2, otherBandMag2),np.subtract(bandMag, otherBandMag),  marker='.', s=0.1)
    plt.ylabel(band1Entry.get()+' - '+band2Entry.get())
    plt.xlabel(band3Entry.get()+' - '+band4Entry.get())
    plt.title('Color Color Diagram')
    plt.xlim((-1.5, 2.75))
    plt.ylim((-2, 2))
    return plt.show()



#######################
# Tk part2   #
#######################
from Tkinter import Tk, W, E
from ttk import Frame, Button, Label, Style
from ttk import Entry

the_window = tk.Tk()
frame = Frame(the_window)
      

Style().configure("TButton", padding=(0, 5, 0, 5), 
    font='serif 10')

frame.columnconfigure(0, pad=3)
frame.columnconfigure(1, pad=3)
frame.columnconfigure(2, pad=3)
frame.columnconfigure(3, pad=3)

frame.rowconfigure(0, pad=3)
frame.rowconfigure(1, pad=3)
##  ENTRY  ###
band1Label = Label(frame, text='Band 1')
band1Label.grid(row=0, column=0)
band1Entry = Entry(frame)
band1Entry.grid(row=0, column=1)
band2Label = Label(frame, text='Band 2')
band2Label.grid(row=0, column=2)
band2Entry = Entry(frame)
band2Entry.grid(row=0, column=3 )
band3Label = Label(frame, text='Band 3')
band3Label.grid(row=1, column=0)
band3Entry = Entry(frame)
band3Entry.grid(row=1, column=1)
band4Label = Label(frame, text='Band 4')
band4Label.grid(row=1, column=2)
band4Entry = Entry(frame)
band4Entry.grid(row=1, column=3 )

CatalogLabel = Label(frame, text='Catalog Path')
CatalogLabel.grid(row=1, column=4)
CatalogEntry = Entry(frame)
CatalogEntry.grid(row=1, column=5 )


##  BUTTONS  ###
sizeMagButton = Button(frame, text ="Size Magnitude", command = sizeMag)
sizeMagButton.grid(row=2  , column = 0)

hrButton = Button(frame, text ="H-R Diagram", command = HR)
hrButton.grid(row=2  , column = 1)

colorColorButton = Button(frame, text='Color Color', command=colorColor)
colorColorButton.grid(row=2  , column = 2)

LoadCatalogButton = Button(frame, text='Load Catalog', command=LoadCatalog)
LoadCatalogButton.grid(row=2  , column = 5)
        
frame.pack()

the_window.mainloop()

  
