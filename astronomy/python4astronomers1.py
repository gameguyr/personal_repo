#! /usr/bin/python2.7

#####################
# PURPOSE: to learn the first workshop in the python4astronomes
#
# DATE: 11/9/2013
#
# AUTHOR: Russell Lego
####################

from astropy.table import Table
import astropy.coordinates as coords
import astropy.units as u
import matplotlib.pylab as plot

filename='/Users/rlego/Dropbox/PythonWorkspace/py4ast/install/table1.dat'
data = Table.read(filename,format='ascii')
ra=data['RAdeg']
dec=data['DEdeg']
plot.scatter(ra, dec, marker='.', color='blue')

coords.RA