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


#filePath = '/Users/rlego/Dropbox/PythonWorkspace/lowzPython/lowz.fits'

#filePath = '/Users/rlego/Dropbox/final_search/fin_cat.fits'
#catList = pf.open(filePath)

#catData = catList[1].data


####################
# making some variables
####################

c = 3.0E5
h = 100.0
fname = '/Users/rlego/Dropbox/PythonWorkspace/SdssFlagsDict.sav'
file = open(fname, 'r')
FlagsDict = pickle.load(file)
file.close()




####################
# defining some functions
####################



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
    
def FlagMaker():
    pass
    

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

##  Check Buttons  ###
frame2 = Frame(the_window)
BLENDEDVar = tk.IntVar()
BLENDEDCheck = tk.Checkbutton(frame2, text='BLENDED', variable=BLENDEDVar)
BLENDEDCheck.grid(row=0, column=0)
DEBLENDED_AS_MOVINGVar = tk.IntVar()
DEBLENDED_AS_MOVINGCheck = tk.Checkbutton(frame2, text='DEBLENDED_AS_MOVING', variable=DEBLENDED_AS_MOVINGVar)
DEBLENDED_AS_MOVINGCheck.grid(row=1, column=0)
NOPROFILEVar = tk.IntVar()
NOPROFILECheck = tk.Checkbutton(frame2, text='NOPROFILE', variable=NOPROFILEVar)
NOPROFILECheck.grid(row=2, column=0)
BINNED4Var = tk.IntVar()
BINNED4Check = tk.Checkbutton(frame2, text='BINNED4', variable=BINNED4Var)
BINNED4Check.grid(row=3, column=0)
ELLIPFAINTVar = tk.IntVar()
ELLIPFAINTCheck = tk.Checkbutton(frame2, text='ELLIPFAINT', variable=ELLIPFAINTVar)
ELLIPFAINTCheck.grid(row=4, column=0)
INTERPVar = tk.IntVar()
INTERPCheck = tk.Checkbutton(frame2, text='INTERP', variable=INTERPVar)
INTERPCheck.grid(row=5, column=0)
BAD_MOVING_FIT_CHILDVar = tk.IntVar()
BAD_MOVING_FIT_CHILDCheck = tk.Checkbutton(frame2, text='BAD_MOVING_FIT_CHILD', variable=BAD_MOVING_FIT_CHILDVar)
BAD_MOVING_FIT_CHILDCheck.grid(row=6, column=0)
NOTCHECKED_CENTERVar = tk.IntVar()
NOTCHECKED_CENTERCheck = tk.Checkbutton(frame2, text='NOTCHECKED_CENTER', variable=NOTCHECKED_CENTERVar)
NOTCHECKED_CENTERCheck.grid(row=7, column=0)
LOCAL_EDGEVar = tk.IntVar()
LOCAL_EDGECheck = tk.Checkbutton(frame2, text='LOCAL_EDGE', variable=LOCAL_EDGEVar)
LOCAL_EDGECheck.grid(row=0, column=1)
BRIGHTVar = tk.IntVar()
BRIGHTCheck = tk.Checkbutton(frame2, text='BRIGHT', variable=BRIGHTVar)
BRIGHTCheck.grid(row=1, column=1)
SATUR_CENTERVar = tk.IntVar()
SATUR_CENTERCheck = tk.Checkbutton(frame2, text='SATUR_CENTER', variable=SATUR_CENTERVar)
SATUR_CENTERCheck.grid(row=2, column=1)
DEBLEND_TOO_MANY_PEAKSVar = tk.IntVar()
DEBLEND_TOO_MANY_PEAKSCheck = tk.Checkbutton(frame2, text='DEBLEND_TOO_MANY_PEAKS', variable=DEBLEND_TOO_MANY_PEAKSVar)
DEBLEND_TOO_MANY_PEAKSCheck.grid(row=3, column=1)
HAS_CENTERVar = tk.IntVar()
HAS_CENTERCheck = tk.Checkbutton(frame2, text='HAS_CENTER', variable=HAS_CENTERVar)
HAS_CENTERCheck.grid(row=4, column=1)
MANYPETROVar = tk.IntVar()
MANYPETROCheck = tk.Checkbutton(frame2, text='MANYPETRO', variable=MANYPETROVar)
MANYPETROCheck.grid(row=5, column=1)
NOSTOKESVar = tk.IntVar()
NOSTOKESCheck = tk.Checkbutton(frame2, text='NOSTOKES', variable=NOSTOKESVar)
NOSTOKESCheck.grid(row=6, column=1)
INTERP_CENTERVar = tk.IntVar()
INTERP_CENTERCheck = tk.Checkbutton(frame2, text='INTERP_CENTER', variable=INTERP_CENTERVar)
INTERP_CENTERCheck.grid(row=7, column=1)
AMOMENT_MAXITERVar = tk.IntVar()
AMOMENT_MAXITERCheck = tk.Checkbutton(frame2, text='AMOMENT_MAXITER', variable=AMOMENT_MAXITERVar)
AMOMENT_MAXITERCheck.grid(row=0, column=2)
SATURATEDVar = tk.IntVar()
SATURATEDCheck = tk.Checkbutton(frame2, text='SATURATED', variable=SATURATEDVar)
SATURATEDCheck.grid(row=1, column=2)
COSMIC_RAYVar = tk.IntVar()
COSMIC_RAYCheck = tk.Checkbutton(frame2, text='COSMIC_RAY', variable=COSMIC_RAYVar)
COSMIC_RAYCheck.grid(row=2, column=2)
BAD_RADIALVar = tk.IntVar()
BAD_RADIALCheck = tk.Checkbutton(frame2, text='BAD_RADIAL', variable=BAD_RADIALVar)
BAD_RADIALCheck.grid(row=3, column=2)
PEAKCENTERVar = tk.IntVar()
PEAKCENTERCheck = tk.Checkbutton(frame2, text='PEAKCENTER', variable=PEAKCENTERVar)
PEAKCENTERCheck.grid(row=4, column=2)
NOTCHECKEDVar = tk.IntVar()
NOTCHECKEDCheck = tk.Checkbutton(frame2, text='NOTCHECKED', variable=NOTCHECKEDVar)
NOTCHECKEDCheck.grid(row=5, column=2)
AMOMENT_SHIFTVar = tk.IntVar()
AMOMENT_SHIFTCheck = tk.Checkbutton(frame2, text='AMOMENT_SHIFT', variable=AMOMENT_SHIFTVar)
AMOMENT_SHIFTCheck.grid(row=6, column=2)
DEBLENDED_AS_PSFVar = tk.IntVar()
DEBLENDED_AS_PSFCheck = tk.Checkbutton(frame2, text='DEBLENDED_AS_PSF', variable=DEBLENDED_AS_PSFVar)
DEBLENDED_AS_PSFCheck.grid(row=7, column=2)
TOO_LARGEVar = tk.IntVar()
TOO_LARGECheck = tk.Checkbutton(frame2, text='TOO_LARGE', variable=TOO_LARGEVar)
TOO_LARGECheck.grid(row=0, column=3)
BADSKYVar = tk.IntVar()
BADSKYCheck = tk.Checkbutton(frame2, text='BADSKY', variable=BADSKYVar)
BADSKYCheck.grid(row=1, column=3)
BINNED2Var = tk.IntVar()
BINNED2Check = tk.Checkbutton(frame2, text='BINNED2', variable=BINNED2Var)
BINNED2Check.grid(row=2, column=3)
SUBTRACTEDVar = tk.IntVar()
SUBTRACTEDCheck = tk.Checkbutton(frame2, text='SUBTRACTED', variable=SUBTRACTEDVar)
SUBTRACTEDCheck.grid(row=3, column=3)
BAD_COUNTS_ERRORVar = tk.IntVar()
BAD_COUNTS_ERRORCheck = tk.Checkbutton(frame2, text='BAD_COUNTS_ERROR', variable=BAD_COUNTS_ERRORVar)
BAD_COUNTS_ERRORCheck.grid(row=4, column=3)
STATIONARYVar = tk.IntVar()
STATIONARYCheck = tk.Checkbutton(frame2, text='STATIONARY', variable=STATIONARYVar)
STATIONARYCheck.grid(row=5, column=3)
CANONICAL_CENTERVar = tk.IntVar()
CANONICAL_CENTERCheck = tk.Checkbutton(frame2, text='CANONICAL_CENTER', variable=CANONICAL_CENTERVar)
CANONICAL_CENTERCheck.grid(row=6, column=3)
PSF_FLUX_INTERPVar = tk.IntVar()
PSF_FLUX_INTERPCheck = tk.Checkbutton(frame2, text='PSF_FLUX_INTERP', variable=PSF_FLUX_INTERPVar)
PSF_FLUX_INTERPCheck.grid(row=7, column=3)
NODEBLENDVar = tk.IntVar()
NODEBLENDCheck = tk.Checkbutton(frame2, text='NODEBLEND', variable=NODEBLENDVar)
NODEBLENDCheck.grid(row=0, column=4)
RESERVEDVar = tk.IntVar()
RESERVEDCheck = tk.Checkbutton(frame2, text='RESERVED', variable=RESERVEDVar)
RESERVEDCheck.grid(row=1, column=4)
MAYBE_EGHOSTVar = tk.IntVar()
MAYBE_EGHOSTCheck = tk.Checkbutton(frame2, text='MAYBE_EGHOST', variable=MAYBE_EGHOSTVar)
MAYBE_EGHOSTCheck.grid(row=2, column=4)
DEBLEND_UNASSIGNED_FLUXVar = tk.IntVar()
DEBLEND_UNASSIGNED_FLUXCheck = tk.Checkbutton(frame2, text='DEBLEND_UNASSIGNED_FLUX', variable=DEBLEND_UNASSIGNED_FLUXVar)
DEBLEND_UNASSIGNED_FLUXCheck.grid(row=3, column=4)
DEBLENDED_AT_EDGEVar = tk.IntVar()
DEBLENDED_AT_EDGECheck = tk.Checkbutton(frame2, text='DEBLENDED_AT_EDGE', variable=DEBLENDED_AT_EDGEVar)
DEBLENDED_AT_EDGECheck.grid(row=4, column=4)
CENTER_OFF_AIMAGEVar = tk.IntVar()
CENTER_OFF_AIMAGECheck = tk.Checkbutton(frame2, text='CENTER_OFF_AIMAGE', variable=CENTER_OFF_AIMAGEVar)
CENTER_OFF_AIMAGECheck.grid(row=5, column=4)
BINNED1Var = tk.IntVar()
BINNED1Check = tk.Checkbutton(frame2, text='BINNED1', variable=BINNED1Var)
BINNED1Check.grid(row=6, column=4)
MOVEDVar = tk.IntVar()
MOVEDCheck = tk.Checkbutton(frame2, text='MOVED', variable=MOVEDVar)
MOVEDCheck.grid(row=7, column=4)
MAYBE_CRVar = tk.IntVar()
MAYBE_CRCheck = tk.Checkbutton(frame2, text='MAYBE_CR', variable=MAYBE_CRVar)
MAYBE_CRCheck.grid(row=0, column=5)
INCOMPLETE_PROFILEVar = tk.IntVar()
INCOMPLETE_PROFILECheck = tk.Checkbutton(frame2, text='INCOMPLETE_PROFILE', variable=INCOMPLETE_PROFILEVar)
INCOMPLETE_PROFILECheck.grid(row=1, column=5)
DEBLEND_PRUNEDVar = tk.IntVar()
DEBLEND_PRUNEDCheck = tk.Checkbutton(frame2, text='DEBLEND_PRUNED', variable=DEBLEND_PRUNEDVar)
DEBLEND_PRUNEDCheck.grid(row=2, column=5)
NODEBLEND_MOVINGVar = tk.IntVar()
NODEBLEND_MOVINGCheck = tk.Checkbutton(frame2, text='NODEBLEND_MOVING', variable=NODEBLEND_MOVINGVar)
NODEBLEND_MOVINGCheck.grid(row=3, column=5)
BAD_MOVING_FITVar = tk.IntVar()
BAD_MOVING_FITCheck = tk.Checkbutton(frame2, text='BAD_MOVING_FIT', variable=BAD_MOVING_FITVar)
BAD_MOVING_FITCheck.grid(row=4, column=5)
BRIGHTEST_GALAXY_CHILDVar = tk.IntVar()
BRIGHTEST_GALAXY_CHILDCheck = tk.Checkbutton(frame2, text='BRIGHTEST_GALAXY_CHILD', variable=BRIGHTEST_GALAXY_CHILDVar)
BRIGHTEST_GALAXY_CHILDCheck.grid(row=5, column=5)
DEBLEND_DEGENERATEVar = tk.IntVar()
DEBLEND_DEGENERATECheck = tk.Checkbutton(frame2, text='DEBLEND_DEGENERATE', variable=DEBLEND_DEGENERATEVar)
DEBLEND_DEGENERATECheck.grid(row=6, column=5)
TOO_FEW_GOOD_DETECTIONSVar = tk.IntVar()
TOO_FEW_GOOD_DETECTIONSCheck = tk.Checkbutton(frame2, text='TOO_FEW_GOOD_DETECTIONS', variable=TOO_FEW_GOOD_DETECTIONSVar)
TOO_FEW_GOOD_DETECTIONSCheck.grid(row=7, column=5)
MANYR90Var = tk.IntVar()
MANYR90Check = tk.Checkbutton(frame2, text='MANYR90', variable=MANYR90Var)
MANYR90Check.grid(row=0, column=6)
OBJECT2_DEBLEND_PEEPHOLEVar = tk.IntVar()
OBJECT2_DEBLEND_PEEPHOLECheck = tk.Checkbutton(frame2, text='OBJECT2_DEBLEND_PEEPHOLE', variable=OBJECT2_DEBLEND_PEEPHOLEVar)
OBJECT2_DEBLEND_PEEPHOLECheck.grid(row=1, column=6)
DEBLEND_NOPEAKVar = tk.IntVar()
DEBLEND_NOPEAKCheck = tk.Checkbutton(frame2, text='DEBLEND_NOPEAK', variable=DEBLEND_NOPEAKVar)
DEBLEND_NOPEAKCheck.grid(row=2, column=6)
GROWN_MERGEDVar = tk.IntVar()
GROWN_MERGEDCheck = tk.Checkbutton(frame2, text='GROWN_MERGED', variable=GROWN_MERGEDVar)
GROWN_MERGEDCheck.grid(row=3, column=6)
PEAKS_TOO_CLOSEVar = tk.IntVar()
PEAKS_TOO_CLOSECheck = tk.Checkbutton(frame2, text='PEAKS_TOO_CLOSE', variable=PEAKS_TOO_CLOSEVar)
PEAKS_TOO_CLOSECheck.grid(row=4, column=6)
MANYR50Var = tk.IntVar()
MANYR50Check = tk.Checkbutton(frame2, text='MANYR50', variable=MANYR50Var)
MANYR50Check.grid(row=5, column=6)
TOO_FEW_DETECTIONSVar = tk.IntVar()
TOO_FEW_DETECTIONSCheck = tk.Checkbutton(frame2, text='TOO_FEW_DETECTIONS', variable=TOO_FEW_DETECTIONSVar)
TOO_FEW_DETECTIONSCheck.grid(row=6, column=6)
AMOMENT_FAINTVar = tk.IntVar()
AMOMENT_FAINTCheck = tk.Checkbutton(frame2, text='AMOMENT_FAINT', variable=AMOMENT_FAINTVar)
AMOMENT_FAINTCheck.grid(row=7, column=6)
PETROFAINTVar = tk.IntVar()
PETROFAINTCheck = tk.Checkbutton(frame2, text='PETROFAINT', variable=PETROFAINTVar)
PETROFAINTCheck.grid(row=0, column=7)
EDGEVar = tk.IntVar()
EDGECheck = tk.Checkbutton(frame2, text='EDGE', variable=EDGEVar)
EDGECheck.grid(row=1, column=7)
CANONICAL_BANDVar = tk.IntVar()
CANONICAL_BANDCheck = tk.Checkbutton(frame2, text='CANONICAL_BAND', variable=CANONICAL_BANDVar)
CANONICAL_BANDCheck.grid(row=2, column=7)
CHILDVar = tk.IntVar()
CHILDCheck = tk.Checkbutton(frame2, text='CHILD', variable=CHILDVar)
CHILDCheck.grid(row=3, column=7)
NOPETRO_BIGVar = tk.IntVar()
NOPETRO_BIGCheck = tk.Checkbutton(frame2, text='NOPETRO_BIG', variable=NOPETRO_BIGVar)
NOPETRO_BIGCheck.grid(row=4, column=7)
NOPETROVar = tk.IntVar()
NOPETROCheck = tk.Checkbutton(frame2, text='NOPETRO', variable=NOPETROVar)
NOPETROCheck.grid(row=5, column=7)
OBJECT2_HAS_SATUR_DNVar = tk.IntVar()
OBJECT2_HAS_SATUR_DNCheck = tk.Checkbutton(frame2, text='OBJECT2_HAS_SATUR_DN', variable=OBJECT2_HAS_SATUR_DNVar)
OBJECT2_HAS_SATUR_DNCheck.grid(row=6, column=7)
MEDIAN_CENTERVar = tk.IntVar()
MEDIAN_CENTERCheck = tk.Checkbutton(frame2, text='MEDIAN_CENTER', variable=MEDIAN_CENTERVar)
MEDIAN_CENTERCheck.grid(row=7, column=7)




########################################
# for loop for generating the names of the widgets
########################################


#EndFinal = 8
#StartFinal = 0


#for j in range(0, int(round(math.sqrt(len(dict))))):
#    for i in range(StartFinal, EndFinal): 
#        print dict.keys()[i]+'Var = tk.IntVar()'
#        print dict.keys()[i]+'Check = tk.Checkbutton(frame2, \
#        text='+"'"+dict.keys()[i]+"'"+', variable='+dict.keys()[i]+'Var)'
#        print dict.keys()[i]+'Check.grid(row='+str(i-(8*j))+', column='+str(j)+')'
#    StartFinal = EndFinal
#    EndFinal = StartFinal + 8
    
    
    




########################################
# for making the indices for different slections
########################################


## for comparing hex number and regular
##   int(FlagsDict['BINNED1'],0) & obj['flags'] should give a non-zero number 
##   if 'flags' have BINNED1 flag set


frame3 = Frame(the_window)
OverPlotVar = tk.IntVar()
OverPlotCheck = tk.Checkbutton(frame2,text='MEDIAN_CENTER', variable=MEDIAN_CENTERVar)
OverPlotCheck.grid(row=7, column=7)







##  starting the GUI APP  ###
frame.pack()
frame2.pack()

the_window.mainloop()

  
