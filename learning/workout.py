#! /usr/bin/python2.7

#####################
# PURPOSE: 
#
# DATE: 
#
# AUTHOR: Russell Lego
####################

import Tkinter as tk
import ttk
import Image as image
from random import randrange
import os


path = '/Users/rlego/Dropbox/PythonWorkspace/ActivityImages'
struct={'swim': 'swim.png', 'bike': 'bike.png', 'run': 'run.png', 'hike': 'hike.png',\
'gym': 'gym.png', 'disc': 'disc.png', 'elliptical': 'elliptical.png', 'yoga': \
'yoga.png', 'p90x': 'p90x.png'}

print''
print' Are you ready to workout?'
print''

decision=raw_input('Please enter the y/n:   ')
if decision == 'y':
    number = randrange(len(struct)-1)
    workoutImage = image.open(path+'/'+struct[struct.keys()[number]])
    workoutImage.show()
else:
    print ''
    print 'Well come back when you are ready!!'
    print''
                           