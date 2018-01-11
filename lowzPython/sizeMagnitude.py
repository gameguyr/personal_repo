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


filePath = '/Users/rlego/IDLWorkspace/Default/lowz_project/lowz.fits'

catList = pf.open(filePath)

catData = catList[1].data
#######################
# DEFINING CONSTANTS  #
#######################
c = 3.0E5
h = 100.0

def balls(x):
    print str(x)+'balls'

rMag = map( lambda x:x[2], catData.field('ABSMAG'))

def sizeMag():
    size = (c/h)*catData.field('ZDIST')*(catData.field('PETROTH50')/float(206265))
    plt.scatter(size, rMag, marker='.')
    return plt.show()
    
