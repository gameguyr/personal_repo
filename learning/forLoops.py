# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:01:23 2013

@author: rlego
"""
#PURPOSE: 
#testing for loops
#
import pyfits
import numpy as np

filename1='/Users/rlego/Dropbox/Research/KPNO/som1sex.fits'
filename2='/Users/rlego/Dropbox/Research/KPNO/som2sex.fits'

list1=pyfits.open(filename1)
list2=pyfits.open(filename2)
data1=list1[2].data
data2=list2[2].data
ra1=data1['ALPHA_J2000']
ra2=data2['ALPHA_J2000']
dec1=data1['DELTA_J2000']
dec2=data2['DELTA_J2000']
ra=np.concatenate((ra1, ra2))
dec=np.concatenate((dec1, dec2))

regionLines = ['# Region file format: DS9 version 4.1', \
'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1',\
'fk5']
preRegionString = 'circle( '
midRegionString  = ','
postmidRegionString=',4.5") # color=red tag={Collection} \n'



for i in range(0, len(ra)):
    regionLines.append( preRegionString+str(ra[i])+midRegionString+str(dec[i])+postmidRegionString ) 
    