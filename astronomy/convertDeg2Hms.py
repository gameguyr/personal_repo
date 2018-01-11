#! /usr/bin/python2.7

#####################
# PURPOSE: to convert a list of ra and dec in degrees into sexigesimal
#
# DATE: 11/9/2013
#
# AUTHOR: Russell Lego
####################

from astropy.table import Table
import astropysics.coords

#import astropy.coordinates as coords
#import astropy.units as u
#import matplotlib.pylab as plot

filename='/Users/rlego/Dropbox/Research/KPNO/matchedAngle1.txt'
#filename=''
#filename=raw_input('enter the name of the file  :  ')
data = Table.read(filename,format='ascii')

raDeg= data['col1']
decDeg= data['col2']
raSex = []
decSex = []
raSexColon=[]
decSexColon=[]

for ra, dec in zip(raDeg, decDeg):
    raSex.append(astropysics.coords.AngularCoordinate(ra).hms)
    decSex.append(astropysics.coords.AngularCoordinate(dec).dms)
#    print astropysics.coords.AngularCoordinate(dec).dms
#    print i, j

for ra, dec, in zip(raSex, decSex):
    raSexColon.append(str(ra[0])+':'+str(ra[1])+':'+str(ra[2])) 
    decSexColon.append(str(dec[0])+':'+str(dec[1])+':'+str(dec[2]))
fileoutname=filename[:-3]+'reg'

region=['# Region file format: DS9 version 4.1', 'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1', \
'fk5']
#region=[]
for ra, dec, in zip(raSexColon, decSexColon):
    region.append('circle('+ra+', '+dec+', 4.5") # color=red tag={Collection}')
    
file=open(fileoutname, 'w')

for string in region:
    file.write(string+'\n')
    
file.close()
