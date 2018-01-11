# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:40:51 2013

@author: rlego

@author: rlego
"""
#PURPOSE: 
#converting degrees and testing efficiency
#

from astropy.table import Table
import numpy as np

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
