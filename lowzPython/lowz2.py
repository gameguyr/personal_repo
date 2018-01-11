#! /usr/bin/python2.7

#####################
# PURPOSE:to visualize the lowz catalog SDSS
#
# DATE:4/20/2013
#
# AUTHOR: Russell Lego
####################

import pyfits as pf
import matplotlib.pylab as plt
import numpy as np
import Tkinter as tk
import tkMessageBox as mb
import ttk


#filePath = '/home/rlego/Dropbox/PythonWorkspace/lowzPython/lowz.fits'
filePath = '/Users/rlego/Dropbox/PythonWorkspace/lowzPython/lowz.fits'
catList = pf.open(filePath)

catData = catList[1].data
#######################
# DEFINING CONSTANTS  #
#######################
c = 3.0E5
h = 100.0
#distance = map(lambda x:(c/h)*x, catData.field('ZDIST'))
#rMag = map( lambda x:x[2], catData.field('ABSMAG'))
#r50 = map( lambda x:x[2]/float(206265), catData.field('PETROTH50'))
#size = np.multiply(r50, np.dot(distance, 1E6))




#######################
# Functions  #
#######################
def bandSelector(band):
    if band=='u':
        bandNumber=0
    if band=='g':
        bandNumber=1
    if band=='r':
        bandNumber=2
    if band=='i':
        bandNumber=3
    if band=='z':
        bandNumber=4
    return bandNumber

def size():
    #distance in parsecs
    #bandNumber = bandSelector(band)
    bandNumber = bandSelector(bandEntry.get())
    
    r50 = map( lambda x:x[bandNumber]/float(206265), catData.field('PETROTH50'))
    
    distance = np.dot(catData.field('ZDIST'), (c/h)*1E6)
    size = np.multiply(np.dot(r50, 1/float(206265)), distance)
    return size
        
def sizeMag():
    #bandNumber = bandSelector(band)
    bandNumber = bandSelector(bandEntry.get())
    bandMag = map(lambda x:x[bandNumber], catData.field('ABSMAG'))
    r50 = map(lambda x:x[bandNumber]/float(206265), catData.field('PETROTH50'))
    distance = np.dot(catData.field('ZDIST'), (c/h)*1E6)
    size = np.multiply(np.dot(r50, 1/float(206265)), distance)
    plt.scatter(bandMag, np.log10(size),  marker='.', s=0.1)
    plt.ylabel('Half Light Radius [Parsecs]')
    plt.xlabel('Absolute Magnitude')
    plt.title('Size Magnitude Diagram')
    plt.xlim((-23, -12))
    plt.ylim((-3.25, -1.25))
    return plt.show()
    
def HR():
    bandNumber = bandSelector(bandEntry.get())
    otherBandNumber = bandSelector(otherBandEntry.get())
    bandMag = map(lambda x:x[bandNumber], catData.field('ABSMAG'))
    otherBandMag = map(lambda x:x[otherBandNumber], catData.field('ABSMAG'))
    plt.scatter(np.subtract(bandMag, otherBandMag), bandMag,  marker='.', s=0.1)
    plt.ylabel('Absolute Magnitude   '+bandEntry.get()+' Band')
    plt.xlabel(bandEntry.get()+' - '+otherBandEntry.get())
    plt.title('H-R Diagram')
    plt.xlim((-0.25, 1.25))
    plt.ylim((-23, -11))
    return plt.show()


def colorColor():
    bandNumber = bandSelector(bandEntry.get())
    otherBandNumber = bandSelector(otherBandEntry.get())
    bandNumber2 = bandSelector(bandEntry2.get())
    otherBandNumber2 = bandSelector(otherBandEntry2.get())
    bandMag = map(lambda x:x[bandNumber], catData.field('ABSMAG'))
    otherBandMag = map(lambda x:x[otherBandNumber], catData.field('ABSMAG'))
    bandMag2 = map(lambda x:x[bandNumber2], catData.field('ABSMAG'))
    otherBandMag2 = map(lambda x:x[otherBandNumber2], catData.field('ABSMAG'))
    plt.scatter(np.subtract(bandMag, otherBandMag), np.subtract(bandMag2, otherBandMag2),  marker='.', s=0.1)
    plt.ylabel(bandEntry.get()+' - '+otherBandEntry.get())
    plt.xlabel(bandEntry2.get()+' - '+otherBandEntry2.get())
    plt.title('H-R Diagram')
    plt.xlim((-1.5, 2.75))
    plt.ylim((-2, 2))

    return plt.show()


    
#######################
# Tk part  #
#######################
the_window = tk.Tk()


    #######################
    # Widgets  #
    #######################
bandEntry=tk.Entry(the_window)
bandEntry.grid(row=0, column=0)
otherBandEntry = tk.Entry(the_window)
otherBandEntry.grid(row=0, column=1)

bandEntry2 = tk.Entry(the_window)
bandEntry2.grid(row=1, column=0)
otherBandEntry2 = tk.Entry(the_window)
otherBandEntry2.grid(row=1, column=1)

label = tk.Label(the_window, text='Menu Window', font=("Helvetica", 18))

bandLabel = tk.Label(the_window, text='band')
otherBandLabel = tk.Label(the_window, text='other band')

sizeMagButton = tk.Button(the_window, text ="Size Magnitude", command = sizeMag)
hrButton = tk.Button(the_window, text ="H-R Diagram", command = HR)
colorColorButton = tk.Button(the_window, text='Color Color', command=colorColor)



label.pack()
bandLabel.pack()
bandEntry.pack()
otherBandLabel.pack()
otherBandEntry.pack()
sizeMagButton.pack()
hrButton.pack()
bandEntry2.pack()
otherBandEntry2.pack()
colorColorButton.pack()




the_window.mainloop()


    

    
