#! /usr/bin/python2.7

#Reading in the coordinates of the 

import numpy as np
import pickle
c = 3E5
h = 72

raNGC5846 = 187.0732283*np.pi/180
decNGC5846 = 12.667189*np.pi/180


x = np.cos(decNGC5846) * np.cos(raNGC5846)
y = np.cos(decNGC5846) * np.sin(raNGC5846)
rNGC5846 = np.sqrt(x**2 + y**2)

fileName = '/home/rlego/Documents/PythonWorkspace/NGC5846Coordinates.sav'
file = open(fileName, 'w')
pickle.dump(rNGC5846, file)


