#! /usr/bin/python2.7

#####################
# PURPOSE: To automate reduction of images using iraf w/python
#
# DATE: 6/27/2013
#
# AUTHOR: Russell Lego
####################

from pyraf import iraf
import numpy as np


# getting the names of the files to reduce
M51ListFile = '/Users/rlego/Dropbox/leuschner/2013.04.10/SCIENCE/raw/M51.list'
file = open(M51ListFile, 'r')
RawFileNames = file.readlines()
file.close()

#loading the Dark frame  (the Dark is already bias subtracted)
DarkFileName = '/Users/rlego/Dropbox/leuschner/2013.04.10/DARKS/dark_bias180s.fits'

#Loading the bias frame
BiasFileName = '/Users/rlego/Dropbox/leuschner/2013.04.10/BIASES/bias.fits'

#loading the flat file list
FlatFileList = '/Users/rlego/Dropbox/leuschner/2013.04.10/FLATS/FileList.dat'





#running through the loop of subtracting all the sheeze

for i in range(0, np.size(RawFileNames)):
    
    iraf.imarith(operand1 = RawFileNames[i][:-1] ,op='-', \
    operand2 = DarkFileName, result=RawFileNames[i][:-6]+'DarkSub')
    
    iraf.imarith(operand1 = RawFileNames[i][:-6]+'DarkSub' ,op='-',\
    operand2 = BiasFileName, result=RawFileNames[i][:-6]+'BiasAndDarkSub')
    
    
    
def FlatStacker(ListOfFiles):
    iraf.imcombine(input='@'+ListOfFiles output='flat_V combine=median scale=mode