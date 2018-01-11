#! /usr/bin/python2.7

#####################
# PURPOSE: to learn how to write grids using 2 for loops                
#
# DATE: 7/3/2013
#
# AUTHOR: Russell Lego
####################

import numpy as np


list = np.arange(0, 64)
count=0
while count < len(list):
    count2=0
    while count2 < 3:
        print str(list[count+count2])  +' '+str(list[count+count2+1])+' '+str(list[count+count2+2])
        count2+=3
    count = count+count2