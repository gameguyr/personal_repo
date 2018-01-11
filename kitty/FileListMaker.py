#! /usr/bin/python2.7

#####################
# PURPOSE: To mkae a list of file names for IRAF
#
# DATE: 6/18/2013
#
# AUTHOR: Russell Lego
####################

import numpy as np
import os 


path = raw_input('''
Please Enter the File Path
''')

#path = '/Users/rlego/Dropbox/Research/practiceFits/spectemplates'

namesOfFiles = os.listdir(path)
newNamesOfFiles = []
for i in range(0, np.size(namesOfFiles)):
    newNamesOfFiles.append(path+'/'+namesOfFiles[i])
    
filename = path+'/FileList.dat' 
np.savetxt(filename, newNamesOfFiles, fmt='%s')