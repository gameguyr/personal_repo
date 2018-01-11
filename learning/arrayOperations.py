#! /usr/bin/python2.7

#####################
# PURPOSE:to show array operations
#
# DATE:4/23/2013
#
# AUTHOR: Russell Lego
####################

import pyfits as pf
import numpy as np

filePath = '/Users/rlego/Dropbox/PythonWorkspace/lowzPython/lowz.fits'
#telling pyfits to open the catalog
catList = pf.open(filePath)
#loading the table element in the list, the 0 is an image element
# and 1 is the table
catData = catList[1].data



#plucking out the redshift
redShift = catData.field('ZDIST')

#Say you want to multiply all the redshifts by 5 
redShift_5 = np.dot(redShift, 5.0)

#say you want the distance to an object  D=C*Z/Ho
c=3.0E5
ho =100
distance = np.dot(redShift, c/ho)




# Now this took a little bit for me to figure out.  See the field names?  
#  Like 'PETROTH50' If you want to see the names type  >>> catData.columns
# And for the ABSMAG field, it itself has magnitudes for each band so it's an 8
# (u, g, r, i, z, j, h, k) element array where each element is an array of 
# magnitudes.  So say you want the r-magnitudes only, we take advantage of the map 
# function and the lambda procedure which let's you define a function on the fly

bandNumber = 2  # for the r filter

              #function                  #the array
rMag = map(lambda x:x[bandNumber], catData.field('ABSMAG'))

#say you want to element wise multiply the distance by the angular size to 
# get the physical size and there's 206265 arcseconds in a radian
halfLightRadius_in_the_R_filter = map(lambda x:x[bandNumber], catData.field('PETROTH50'))

physicalSize = np.multiply(np.dot(halfLightRadius_in_the_R_filter, 1/float(206265)), distance)




# I hope that clears something up.

print ('Have a wonderful Day!!')









