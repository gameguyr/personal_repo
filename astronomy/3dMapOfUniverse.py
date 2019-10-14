#! /usr/bin/python2.7

#####################
# PURPOSE: to visualize the universe
#
# DATE: 6/19/2013
#
# AUTHOR: Russell Lego
####################

import pyfits as pf
import matplotlib.pylab as plt
import numpy as np
import Tkinter as tk
import tkMessageBox as mb
from mpl_toolkits.mplot3d import Axes3D


## loading data
#filePath = '/Users/lego/Dropbox/Programming/PythonWorkspace/allRed.fits'
filePath = '/Users/lego/git/personal_repo/lowzPython/lowz.fits'
catList = pf.open(filePath)
catData = catList[1].data



## defining variables
c = 3.0E5
h = 100.0
#PHI = np.dot(np.dot(catData.field('RA'), 15.0), np.pi/float(180))
#THETA = np.dot(catData.field('DEC'), np.pi/float(180))
##RHO = np.dot(catData.field('Z'), (c/h)*1E6)
#RHO = np.dot(catData.field('ZDIST'), (c/h)*1E6)
#RVECT = RHO *np.cos(THETA)

PHI = np.dot(np.dot(catData.field('RA'), 15.0), np.pi/float(180))
THETA = np.dot(catData.field('DEC'), np.pi/float(180))
#RHO = np.dot(catData.field('Z')[0:15000], (c/h)*1E6)
RHO = np.dot(catData.field('ZDIST'), (c/h)*1E6)
RVECT = RHO *np.cos(THETA)

print '''

Done with the angles and distance'''

#X = RVECT*np.cos(np.dot(catData.field('RA'), 15.0))
#Y = RVECT*np.sin(PHI)
#Z = RHO*np.sin(THETA)

X = RVECT*np.cos(np.dot(catData.field('RA'), 15.0))
Y = RVECT*np.sin(PHI)
Z = RHO*np.sin(THETA)

print '''

Done with Cartesian Coordinates'''

#plotting the graph
fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
plt.scatter(catData.field('RA'), catData.field('DEC'),  marker='o', s=0.01, color='black')
# ax.scatter(X, Y, Z, marker='o', s=0.1, color='black')

# ax.set_xlabel('Distance in Parsecs')
# ax.set_zlabel('Distance in Parsecs')
# ax.set_ylabel('Distance in Parsecs')

plt.xlabel('RA')
plt.ylabel('DEC')

plt.show()