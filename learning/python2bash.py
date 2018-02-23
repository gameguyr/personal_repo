# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:20:45 2013

@author: rlego
"""
# PURPOSE:
# to run sextractor commands from python into the bash terminal


from subprocess import Popen
import os
import numpy as np


def sexRead(filepath):
    '''
    read in a fits image and extract all sources using sextractor and ouput the file
    
    Default output is   filename+'sex.fits'
    
    '''

    os.chdir('/Users/rlego/sextractor')
    Popen(['/usr/local/bin/sex ' + filepath + ' -CATALOG_NAME ' + filepath[:-5] + 'sex.fits -CATALOG_TYPE FITS_LDAC'],
          shell=True)
    print ''
    print 'File being directed to   ', filepath[:-5] + 'sex.fits'


def regionBuilder(filename, raDecimalDegrees, decDecimalDegrees, color):
    '''
    read in numpy arrays of ra dec and make regions for ds9
    regionBuilder(filename, raDecimalDegrees, decDecimalDegrees)
    
    '''
    # defining the first couple of line for
    try:
        color
    except:
        NameError
        color = 'red'

    regionLines = ['# Region file format: DS9 version 4.1', \
                   'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1', \
                   'fk5']
    preRegionString = 'circle( '
    midRegionString = ','
    postmidRegionString = ',4.5") # color=' + color + ' tag={Collection}'
    file = open(filename, 'w')
    for i in range(0, len(decDecimalDegrees)):
        ra = str(raDecimalDegrees[i])
        dec = str(decDecimalDegrees[i])
        regionLines.append(preRegionString + ra + midRegionString + dec + postmidRegionString)
    for i in xrange(len(regionLines)):
        file.write(regionLines[i] + ' \n')
    file.close
    print ''
    print 'File being directed to   ' + filename
#        return regionLines
