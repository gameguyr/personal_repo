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
import pickle
import math
import time
# import sqlcl
import pdb


#filePath = '/Users/rlego/Dropbox/PythonWorkspace/lowzPython/lowz.fits'

#filePath = '/Users/rlego/Dropbox/final_search/fin_cat.fits'
#CatList = pf.open(filePath)
#CatData = CatList[1].data


####################
# making some variables
####################

c = 3.0E5
h = 100.0
fname = '/Users/russell.lego/Dropbox/PythonWorkspace/sdss/SdssFlagsDict.sav'
file = open(fname, 'r')
FlagsDict = pickle.load(file)
file.close()

BadFlags=['BLENDED','NOPROFILE','BRIGHT','SATURATED','PEAKCENTER','DEBLEND_NOPEAK','NOTCHECKED', 'TOO_FEW_GOOD_DETECTIONS']

## for comparing hex number and regular
##   int(FlagsDict['BINNED1'],0) & obj['flags'] should give a non-zero number 
##   if 'flags' have BINNED1 flag set


#u = CatData['modelmag_u']-CatData['EXTINCTION_u']
#g = CatData['modelmag_g']-CatData['EXTINCTION_g']
#r = CatData['modelmag_r']-CatData['EXTINCTION_r ']
#i = CatData['modelmag_i']-CatData['EXTINCTION_i']
#z = CatData['modelmag_z']-CatData['EXTINCTION_z']


####################
# defining some functions
####################



def LoadCatalog():
    global CatData
    filePath = CatalogEntry.get()
    CatList = pf.open(filePath)
    CatData = CatList[1].data
    print ''
    print 'Catalog Loaded with '+str(len(CatData))+'  Objects'
    
def rangeLimit():
    if Band1Entry.get() =='u' and Band2Entry.get()=='g'and \
    Band3Entry.get()=='i'and Band4Entry.get()=='z':
        print 'UG IZ huh?'
        plt.xlim((-0.2, 0.6))
        plt.ylim((0.5, 3.0))
    
    
    
def BandSelector(Band):
    if Band=='u':
        BandMag=np.subtract(CatData.field('modelmag_u'),CatData.field('extinction_u'))
    if Band=='g':
        BandMag=np.subtract(CatData.field('modelmag_g'),CatData.field('extinction_g'))
    if Band=='r':
        BandMag=np.subtract(CatData.field('modelmag_r'),CatData.field('extinction_r'))
    if Band=='i':
        BandMag=np.subtract(CatData.field('modelmag_i'),CatData.field('extinction_i'))
    if Band=='z':
        BandMag=np.subtract(CatData.field('modelmag_z'),CatData.field('extinction_z'))
    if Band=='j':
        BandMag=CatData.field('J_1APERMAG3')
    if Band=='h':
        BandMag=CatData.field('HAPERMAG3')
    if Band=='k':
        BandMag=CatData.field('KAPERMAG3')
    return BandMag

def UncertainBandSelector(Band):
    if Band=='u':
        UncertainBandMag=CatData.field('modelmagerr_u')
    if Band=='g':
        UncertainBandMag=CatData.field('modelmagerr_g')
    if Band=='r':
       UncertainBandMag=CatData.field('modelmagerr_r')
    if Band=='i':
        UncertainBandMag=CatData.field('modelmagerr_i')
    if Band=='z':
        UncertainBandMag=CatData.field('modelmagerr_z')
    if Band=='j':
        UncertainBandMag=CatData.field('J_1APERMAG3ERR')
    if Band=='h':
        UncertainBandMag=CatData.field('HAPERMAG3ERR')
    if Band=='k':
        UncertainBandMag=CatData.field('KAPERMAG3ERR')
    return UncertainBandMag

def MagMask():
    Error1 = UncertainBand1Entry.get()
    Error2 = UncertainBand2Entry.get()
    Error3 = UncertainBand3Entry.get()
    Error4 = UncertainBand4Entry.get()
    return [Error1, Error2, Error3, Error4]
    
def SizeMag():
#    CatData = LoadCatalog(CatalogEntry.get())
    BandMag = BandSelector(Band1Entry.get())
    r50 = np.dot(CatData.field('PETROTH50'), 1/float(206265))
    distance = np.dot(CatData.field('Z'), (c/h)*1E6)
    size = np.dot(r50, distance)
    plt.scatter(BandMag, np.log10(size),PlottingVariable.get(), s=SizeVariable.get(), color=ColorVariable.get())
    plt.ylabel('Half Light Radius [Parsecs]')
    plt.xlabel('Absolute Magnitude')
    plt.title('Size Magnitude Diagram')
    plt.xlim((-23, -12))
    plt.ylim((-3.25, -1.25))
    
    
def ShowPlot():
    return plt.show()
    

def HR():
#    CatData = LoadCatalog(CatalogEntry.get())
    BandMag = BandSelector(Band1Entry.get())
    UncertainBandMag = UncertainBandSelector(Band1Entry.get())
    print UncertainBandMag
    
    OtherBandMag = BandSelector(Band2Entry.get())
    OtherUncertainBandMag = UncertainBandSelector(Band2Entry.get())
    ErrorBandMag = float(UncertainBand1Entry.get())
    OtherErrorBandMag = float(UncertainBand2Entry.get())
    index = (UncertainBandMag < ErrorBandMag) & (OtherUncertainBandMag < OtherErrorBandMag)
    print ''
    print 'there are now',  len(BandMag[index]), ' objects'
    plt.scatter(np.subtract(BandMag[index], OtherBandMag[index]), BandMag[index],  \
    PlottingVariable.get(), s=SizeVariable.get(), color=ColorVariable.get())
    plt.ylabel('Absolute Magnitude   '+Band1Entry.get()+' Band')
    plt.xlabel(Band1Entry.get()+' - '+Band2Entry.get())
    plt.title('H-R Diagram')
    plt.xlim((-1, 1))
    plt.ylim((22, 10))
    

def ColorColor():
    
#    CatData = LoadCatalog(CatalogEntry.get())
    BandMag = BandSelector(Band1Entry.get())
    UncertainBandMag = UncertainBandSelector(Band1Entry.get())
    
    
    OtherBandMag = BandSelector(Band2Entry.get())
    OtherUncertainBandMag = UncertainBandSelector(Band2Entry.get())
    
    BandMag2 = BandSelector(Band3Entry.get())
    UncertainBandMag2 = UncertainBandSelector(Band3Entry.get())
    
    OtherBandMag2 = BandSelector(Band4Entry.get())
    OtherUncertainBandMag2 = UncertainBandSelector(Band4Entry.get())
    
    ##checking whether the mag mask flags and badfalgs checks are checked
    if (BadFlagVar.get() == 1) & (MagnitudeMaskVar.get() == 1):
        ErrorBandMag = float(UncertainBand1Entry.get())
        OtherErrorBandMag = float(UncertainBand2Entry.get())
        ErrorBandMag2 = float(UncertainBand3Entry.get())
        OtherErrorBandMag2 = float(UncertainBand4Entry.get())
        
        index1 = (UncertainBandMag < ErrorBandMag) & (OtherUncertainBandMag < OtherErrorBandMag) & \
        (UncertainBandMag2 < ErrorBandMag2) & (OtherUncertainBandMag2 < OtherErrorBandMag2)
    
        index2 = (int(FlagsDict["BLENDED"], 0) & CatData['flags'] == 0)  & \
        (int(FlagsDict["NOPROFILE"], 0) & CatData['flags'] == 0)  & \
        (int(FlagsDict["BRIGHT"], 0) & CatData['flags'] == 0)  & \
        (int(FlagsDict["SATURATED"], 0) & CatData['flags'] == 0)  & \
        (int(FlagsDict["PEAKCENTER"], 0) & CatData['flags'] == 0)  & \
        (int(FlagsDict["DEBLEND_NOPEAK"], 0) & CatData['flags'] == 0)  & \
        (int(FlagsDict["NOTCHECKED"], 0) & CatData['flags'] == 0) & \
        (int(FlagsDict["TOO_FEW_GOOD_DETECTIONS"], 0) & CatData['flags'] == 0)
    
        index = index1 & index2
        
        plt.scatter(np.subtract(BandMag2[index], OtherBandMag2[index]),np.subtract\
        (BandMag[index], OtherBandMag[index]),marker=PlottingVariable.get(), s=SizeVariable.get(), color=ColorVariable.get())
        print ' '
        print 'You now have  ', len(BandMag[index]), ' Objects After the Cut'
        print ' '
        
    else:
        plt.scatter(np.subtract(BandMag2, OtherBandMag2),np.subtract\
        (BandMag, OtherBandMag),marker=PlottingVariable.get(), s=SizeVariable.get(), color=ColorVariable.get())
        
        print ' '
        print 'You Have  ', len(BandMag), ' Total Objects'
        print ' '
    

    
    plt.ylabel(Band1Entry.get()+' - '+Band2Entry.get())
    plt.xlabel(Band3Entry.get()+' - '+Band4Entry.get())
    plt.title('Color Color Diagram')
    
    rangeLimit()
    
    
    
    print ' '
    print 'Ready to Show Plot'
    print ' '
    pdb.set_trace()


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
Band1Label = Label(frame, text='Band 1')
Band1Label.grid(row=0, column=0)
Band1Entry = Entry(frame)
Band1Entry.grid(row=0, column=1)
Band2Label = Label(frame, text='Band 2')
Band2Label.grid(row=0, column=2)
Band2Entry = Entry(frame)
Band2Entry.grid(row=0, column=3 )
Band3Label = Label(frame, text='Band 3')
Band3Label.grid(row=1, column=0)
Band3Entry = Entry(frame)
Band3Entry.grid(row=1, column=1)
Band4Label = Label(frame, text='Band 4')
Band4Label.grid(row=1, column=2)
Band4Entry = Entry(frame)
Band4Entry.grid(row=1, column=3 )

CatalogLabel = Label(frame, text='Catalog Path')
CatalogEntry = Entry(frame)
CatalogLabel.grid(row=0, column=4)
CatalogEntry.grid(row=0, column=5 )

##  Plotting Symbols and color options  ###
SizeVariable = tk.DoubleVar()
SizeVariable.set(0.1) # default value
SizeSymbolLabel = Label(frame, text='Size')
SizeSymbolLabel.grid(row=2, column=4 )
SizeSymbolMenu = tk.OptionMenu(frame, SizeVariable, '0.1','0.5', '1', '5', '10', '25', '40')
SizeSymbolMenu.grid(row=2, column=5 )


PlottingVariable = tk.StringVar()
PlottingVariable.set('.') # default value
PlottingSymbolLabel = Label(frame, text='Symbol')
PlottingSymbolLabel.grid(row=2, column=6 )
PlottingSymbolMenu = tk.OptionMenu(frame, PlottingVariable, '.','-', '--', '-.', ':', ',', \
'o', 'v', '^', '<', '>','1','2','3','4','s', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_')
PlottingSymbolMenu.grid(row=2, column=7 )

ColorVariable = tk.StringVar()
ColorVariable.set('black') # default value
ColorLabel = Label(frame, text='Color')
ColorLabel.grid(row=2, column=8 )
ColorMenu = tk.OptionMenu(frame, ColorVariable, 'blue','green','red','cyan','magenta','yellow', \
'black','white')
ColorMenu.grid(row=2, column=9)




##  BUTTONS  ###
SizeMagButton = Button(frame, text ="Size Magnitude", command = SizeMag)
SizeMagButton.grid(row=2  , column = 0)

hrButton = Button(frame, text ="H-R Diagram", command = HR)
hrButton.grid(row=2  , column = 1)

ColorColorButton = Button(frame, text='Color Color', command=ColorColor)
ColorColorButton.grid(row=2  , column = 2)

ShowPlotButton = Button(frame, text='Show Plot', command=ShowPlot)
ShowPlotButton.grid(row=2  , column = 3)

LoadCatalogButton = Button(frame, text='Load Catalog', command=LoadCatalog)
LoadCatalogButton.grid(row=1  , column = 5)


##  Check Buttons  ###
frame2 = Frame(the_window)
frame2.configure(padding = 30)


BadFlagVar = tk.IntVar()
BadFlagCheck = tk.Checkbutton(frame2, text='BadFlag', variable=BadFlagVar)
BadFlagCheck.grid(row=0, column=0)

MagnitudeMaskVar = tk.IntVar()
MagnitudeMaskCheck = tk.Checkbutton(frame2, text='MagnitudeMask', variable=MagnitudeMaskVar)
MagnitudeMaskCheck.grid(row=0, column=1)

#BRIGHTVar = tk.IntVar()
#BRIGHTCheck = tk.Checkbutton(frame2, text='BRIGHT', variable=BRIGHTVar)
#BRIGHTCheck.grid(row=0, column=2)

#SATURATEDVar = tk.IntVar()
#SATURATEDCheck = tk.Checkbutton(frame2, text='SATURATED', variable=SATURATEDVar)
#SATURATEDCheck.grid(row=0, column=3)

#PEAKCENTERVar = tk.IntVar()
#PEAKCENTERCheck = tk.Checkbutton(frame2, text='PEAKCENTER', variable=PEAKCENTERVar)
#PEAKCENTERCheck.grid(row=0, column=4)

#BINNED1Var = tk.IntVar()
#BINNED1Check = tk.Checkbutton(frame2, text='BINNED1', variable=BINNED1Var)
#BINNED1Check.grid(row=0, column=5)

#DEBLEND_NOPEAKVar = tk.IntVar()
#DEBLEND_NOPEAKCheck = tk.Checkbutton(frame2, text='DEBLEND_NOPEAK', variable=DEBLEND_NOPEAKVar)
#DEBLEND_NOPEAKCheck.grid(row=0, column=6)

#NOTCHECKEDVar = tk.IntVar()
#NOTCHECKEDCheck = tk.Checkbutton(frame2, text='NOTCHECKED', variable=NOTCHECKEDVar)
#NOTCHECKEDCheck.grid(row=0, column=7)


######################################################
# Seetting the Uncertainty in the Bands
######################################################
frame3 = Frame(the_window)
frame3.configure(padding = 30)

UncertainBand1Label = Label(frame3, text='UncertainBand 1')
UncertainBand1Label.grid(row=0, column=0)
UncertainBand1Entry = Entry(frame3)
UncertainBand1Entry.grid(row=0, column=1)
UncertainBand2Label = Label(frame3, text='UncertainBand 2')
UncertainBand2Label.grid(row=0, column=2)
UncertainBand2Entry = Entry(frame3)
UncertainBand2Entry.grid(row=0, column=3 )
UncertainBand3Label = Label(frame3, text='UncertainBand 3')
UncertainBand3Label.grid(row=1, column=0)
UncertainBand3Entry = Entry(frame3)
UncertainBand3Entry.grid(row=1, column=1)
UncertainBand4Label = Label(frame3, text='UncertainBand 4')
UncertainBand4Label.grid(row=1, column=2)
UncertainBand4Entry = Entry(frame3)
UncertainBand4Entry.grid(row=1, column=3 )

######################################################
# for getting other attributes besides the flags
######################################################
frame4 = Frame(the_window)
frame4.configure(padding = 30)



OverPlotVar = tk.IntVar()
OverPlotCheck = tk.Checkbutton(frame4,text='OverPlot', variable=OverPlotVar)
OverPlotCheck.grid(row=0, column=0)

StarsVar = tk.IntVar()
StarsCheck = tk.Checkbutton(frame4,text='Stars', variable=StarsVar)
StarsCheck.grid(row=0, column=1)

GalaxiesVar = tk.IntVar()
GalaxiesCheck = tk.Checkbutton(frame4,text='Galaxies', variable=GalaxiesVar)
GalaxiesCheck.grid(row=0, column=2)

Frame3Label = Label(frame, text='Band 1')
Frame3Label.grid(row=0, column=0)







##  starting the GUI APP  ###
frame.pack()
frame2.pack()
frame3.pack()
frame4.pack()

the_window.mainloop()

  
