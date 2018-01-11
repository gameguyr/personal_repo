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
angle2=30.7

###CHANGE THI FILENAME FOR OTHERFILES, COULDN'T FIGURE SOMTHING OUT
### SLASH AND BURN BABY
ra = np.array([189.88173,189.90356, 189.91197])*(np.pi/180)
dec= np.array([-11.606076,-11.627613, -11.624272])*(np.pi/180)
raDeg = np.array([189.88173,189.90356, 189.91197])
decDeg= np.array([-11.606076,-11.627613, -11.624272])


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
masterIndex= np.arange(len(ra))

for i in xrange(len(ra)):
    sep=np.arccos(np.cos(np.pi/2-dec)*np.cos(np.pi/2-dec[i])+\
    np.sin(np.pi/2-dec)*np.sin(np.pi/2-dec[i])*np.cos(ra-ra[i]))*(206265)
    sepCriteria1 = np.abs(sep-angle1) < arcLimit
    sepCriteria2 = np.abs(sep-angle2) < arcLimit
#    sepMatch = sep[(sepCriteria1) & (sepCriteria2)]
    sepCriteriaIndex = sepCriteria1+sepCriteria2
    
#    ra[(sepCriteria1) & (sepCriteria2)]
    if ( len(sep[sepCriteria1])!=0 and len(sep[sepCriteria2])!=0 ):
        hostIndex.append(i)
        print i
#        separation.append(sep[sepCriteriaIndex])
#        pdb.set_trace()
        print sep
        for index in masterIndex[sepCriteriaIndex]:
#        parentRA= np.hstack((parentRA, parentRA[i]))
#            print index
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
childFname='/Users/rlego/Dropbox/Research/KPNO/childIndexTest.reg'
hostFname='/Users/rlego/Dropbox/Research/KPNO/hostIndexTest.reg'


p2b.regionBuilder(hostFname,hostRA, hostDec, 'red' )
p2b.regionBuilder(childFname, childRA,childDEC, 'blue' )

np.abs


print 'DONE!'