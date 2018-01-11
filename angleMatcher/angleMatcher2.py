# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 22:32:40 2013

@author: rlego
"""
#PURPOSE: 
#to calculate angular separations between targets on the sky

import numpy as np
import pyfits
import pdb
import python2bash as p2b
### Defining some angular constrainsts
angle1=124.2
angle2=34.7

###CHANGE THI FILENAME FOR OTHERFILES, COULDN'T FIGURE SOMTHING OUT
### SLASH AND BURN BABY
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
ra=np.concatenate((ra1, ra2))*(np.pi/180)
dec=np.concatenate((dec1, dec2))*(np.pi/180)
raDeg=np.concatenate((ra1, ra2))
decDeg=np.concatenate((dec1, dec2))


#match={}
#parentRA=np.array([1000000],dtype = float)
#parentDEC=np.array([1000000],dtype = float)
#childRA=np.array([1000000],dtype = float)
#childDEC=np.array([1000000],dtype = float)
hostIndex=[]
childIndex=[]
count=0
arcLimit=2
separation=[]
for i in xrange(len(ra)):
    sep=np.arccos(np.cos(np.pi/2-dec)*np.cos(np.pi/2-dec[i])+\
    np.sin(np.pi/2-dec)*np.sin(np.pi/2-dec[i])*np.cos(ra-ra[i]))*(206265)
    sepCriteria1 = np.abs(sep-angle1) < arcLimit
    sepCriteria2 = np.abs(sep-angle2) < arcLimit
#    sepMatch = sep[(sepCriteria1) & (sepCriteria2)]
    sepCriteriaIndex = np.where(sepCriteria2)
    
#    ra[(sepCriteria1) & (sepCriteria2)]
    if len(sep[sepCriteriaIndex])!=0:
        hostIndex.append(i)
#        separation.append(sep[sepCriteriaIndex])
#        pdb.set_trace()
        for index in sepCriteriaIndex[0]:
#        parentRA= np.hstack((parentRA, parentRA[i]))
            print index
#            pdb.set_trace()
            childIndex.append(index)  
#        parentDEC= np.hstack((parentDEC, parentDEC[i])) 
#        np.concatenate((childRA, childRA[sepCriteriaIndex]))
#        np.concatenate((childDEC, childDEC[sepCriteriaIndex]))        
#        print np.array(data['ALPHA_J2000'])[sepCriteria],\
#        np.array(data['ALPHA_J2000'])[sepCriteria]
#        print sep[sepCriteriaIndex]
hostRA=raDeg[hostIndex]
hostDec=decDeg[hostIndex]
childRA=raDeg[childIndex]
childDEC=decDeg[childIndex]
childFname='/Users/rlego/Dropbox/Research/KPNO/childIndex2.reg'
hostFname='/Users/rlego/Dropbox/Research/KPNO/hostIndex2.reg'


p2b.regionBuilder(childFname,hostRA, hostDec, 'red' )
p2b.regionBuilder(hostFname, childRA,childDEC, 'blue' )

np.abs


print 'DONE!'