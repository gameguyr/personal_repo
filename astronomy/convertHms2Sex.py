#! /usr/bin/python2.7

#####################
# PURPOSE: to convert a list of ra and dec in degrees into sexigesimal
#
# DATE: 11/9/2013
#
# AUTHOR: Russell Lego
####################

from astropy.table import Table
import astropy.coordinates as coords
import astropy.units as u
import matplotlib.pylab as plot

filename='/Users/rlego/Dropbox/Research/KPNO/matchedCoordinates.txt'
data = Table.read(filename,format='ascii')

raDeg= data['col1']
decDeg= data['col2']
raList = []
decList = []
raFinal=[]
decFinal=[]
for ra, dec in zip(raDeg, decDeg):
    raList.append(astropysics.coords.AngularCoordinate(ra).hms)
#    decList.append(astropysics.coords.AngularCoordinate(dec).hms)
    print astropysics.coords.AngularCoordinate(dec).dms
#    print i, j

for ra, dec, in zip(raList, decList):
    raFinal.append(str(ra[0])+':'+str(ra[1])+':'+str(ra[2])) 
    decFinal.append(str(dec[0])+':'+str(dec[1])+':'+str(dec[2]))

#zip()