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
angle3=angle1+angle2

###These are some coordintes that match my logic findr
### I was just testing to see if my logic was working in the boolean sense!!!!!!!!!! DRagonFOrce baby

#ra = np.array([189.88173,189.90356, 189.91197])*(np.pi/180)
#dec= np.array([-11.606076,-11.627613, -11.624272])*(np.pi/180)
#raDeg = np.array([189.88173,189.90356, 189.91197])
#decDeg= np.array([-11.606076,-11.627613, -11.624272])

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
arcLimit=0.5
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
        count+=1
        print count
        hostIndex.append(i)
#        print i
#        separation.append(sep[sepCriteriaIndex])
#        pdb.set_trace()
#        print sep
        for index1, index2 in zip(masterIndex[sepCriteria1], masterIndex[sepCriteria2]):
            
#        parentRA= np.hstack((parentRA, parentRA[i]))
#            print index
#            pdb.set_trace()
            childIndex.append(index1)
            childIndex.append(index2)
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



print 'DONE!'
print count, '   Numberof Hosts FOund!!'