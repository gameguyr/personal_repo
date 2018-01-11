#! /usr/bin/python2.7

#####################
# PURPOSE: to confirm the UCD target at KPNO the sombrero one
#
# DATE: 9/26/2013
#
# AUTHOR: Russell Lego
####################

import pyfits as pf
import matplotlib.pylab as plt
import numpy as np

filePath = '/Users/rlego/Dropbox/Research/KPNO/secondObjWcal.fits'
catList = pf.open(filePath)
catData = catList[1].data