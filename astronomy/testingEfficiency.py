# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:40:54 2013

@author: rlego
"""
#PURPOSE: 
#converting degrees and testing efficiency
#

from astropy.table import Table
#import os
#import pdb
#import astropy.coordinates
#import astropy.units as units
import numpy as np
#import astropysics



#os.system('cd /Users/rlego/Dropbox/Research/KPNO')
#os.system('pwd')
#filename = raw_input('Enter the Rootname of the file   :   ')


### Defining some angular constrainsts
angle1=124.2*(1/206265)*(180/np.pi) #degree
angle2=30.7*(1/206265)*(180/np.pi)  #degree
abs=np.abs
cos=np.cos
pi=np.pi
sqrt=np.sqrt

###CHANGE THI FILENAME FOR OTHERFILES, COULDN'T FIGURE SOMTHING OUT
### SLASH AND BURN BABY
filename = '/Users/rlego/Dropbox/Research/KPNO/somCom.txt'
data=Table.read(filename, format='ascii')
raDeg=data['col1']
decDeg=data['col2']

for i in xrange(0, np.size(raDeg)):  
    print i
    for j in xrange(i+1, np.size(raDeg)):
        Dra = abs(raDeg[i]-raDeg[j])*cos(decDeg[i]*pi/180)
        Ddec = abs(decDeg[i]-decDeg[j])
        Dangle=sqrt(Dra*Dra+Ddec*Ddec)
        print i
        if (Dangle-angle1)/angle1 < 0.1 :
            DangleInArcsecs=Dangle*(pi/180)*206265
            print 'they matched'
            str=''
            print 'separation is   :    %(DangleInArcsecs)s'
#        
#for i in range(0, np.size(raDeg)):  
#    print i
#    
#file=numpy
#xrange()
##ending for loop
#
#
#coord1=astropysics.coords.coordsys.FK5Coordinates((ra, dec))