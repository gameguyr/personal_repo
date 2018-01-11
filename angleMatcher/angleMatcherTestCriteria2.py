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

#ra = np.array([189.88173,189.9194, 189.91197])*(np.pi/180)
#dec= np.array([-11.606076,-11.628598, -11.624272])*(np.pi/180)
#raDeg = np.array([189.88173,189.9194, 189.91197])
#decDeg= np.array([-11.606076,-11.628598, -11.624272])

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

count=0
arcLimit=2
separation=[]
masterIndex= np.arange(len(ra))
lines=['# Region file format: DS9 version 4.1', \
    'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1',\
    'fk5']

for i in xrange(len(ra)):
    childIndex=[]
    sep=np.arccos(np.cos(np.pi/2-dec)*np.cos(np.pi/2-dec[i])+\
    np.sin(np.pi/2-dec)*np.sin(np.pi/2-dec[i])*np.cos(ra-ra[i]))*(206265)
    sepCriteria1 = np.abs(sep-angle1) < arcLimit
    sepCriteria2 = np.abs(sep-angle2) < arcLimit
#    sepMatch = sep[(sepCriteria1) & (sepCriteria2)]
#    sepCriteriaIndex = sepCriteria1+sepCriteria2
    
#    ra[(sepCriteria1) & (sepCriteria2)]
    if ( len(sep[sepCriteria1])!=0 and len(sep[sepCriteria2])!=0 ):
        
#        print count
        hostIndex.append(i)
#        print i
#        separation.append(sep[sepCriteriaIndex])
        
#        print sep
        for index1, index2 in zip(masterIndex[sepCriteria1], masterIndex[sepCriteria2]):
            childIndex.append(index1)
            childIndex.append(index2)
#        raChild=ra[childIndex]
#        decChild=dec[childIndex]
        for j in xrange(len(ra[childIndex])):
            sep=np.arccos(np.cos(np.pi/2-dec[childIndex])*np.cos(np.pi/2-dec[childIndex][j])+\
            np.sin(np.pi/2-dec[childIndex])*np.sin(np.pi/2-dec[childIndex][j])*\
            np.cos(ra[childIndex]-ra[childIndex][j]))*(206265)
            
            sepCriteria3 = np.abs(sep-angle3) < arcLimit
            if ( len(sep[sepCriteria3])!=0 ):
                count+=1
#                print 'the current count is   ', count
#                print 'the separation is   ', sep[sepCriteria3]
                index = np.where(sepCriteria3 != 0)
                a='circle('+str(raDeg[i])+','+str(decDeg[i])+',4.5") # color=red tag={Collection}'
                b='circle('+str(raDeg[childIndex][j])+','+str(decDeg[childIndex][j])+',4.5") # color=blue tag={Collection}'
                c='circle('+str(raDeg[childIndex][index][0])+', '+str(decDeg[childIndex][index][0])+',4.5") # color=blue tag={Collection}'
                
                lines.append(a)
                lines.append(b)
                lines.append(c)
#                pdb.set_trace()
                
                
#hostRA=raDeg[hostIndex]
#hostDec=decDeg[hostIndex]
#childRA=raDeg[childIndex]
#childDEC=decDeg[childIndex]
#childFname='/Users/rlego/Dropbox/Research/KPNO/childIndexTest.reg'
#hostFname='/Users/rlego/Dropbox/Research/KPNO/hostIndexTest.reg'
#
#
#p2b.regionBuilder(hostFname,hostRA, hostDec, 'red' )
#p2b.regionBuilder(childFname, childRA,childDEC, 'blue' )
fname='/Users/rlego/Dropbox/Research/KPNO/testMatchCriteria3(current!!).reg'

file=open(fname, 'w')
for line in lines:    
    file.writelines(line+'\n')
file.close()


print 'DONE!'
print count, '   Numberof Hosts FOund!!'