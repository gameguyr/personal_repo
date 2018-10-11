#!/usr/bin/python
########################
# TITLE: sdss_common
# AUTHOR: russell lego
# DATE: 2018-10-10
# PURPOSE: This is a library that will hold all the commonly used function that I
# use in working with the sloan digital sky survey
########################


#################################
# Importing Modules
#################################
import astropy.io.fits as pyfits

#################################
# Defining Constants
#################################


#################################
# Defining Functions
#################################
def load_fits_file(file_path):

    fits_file_list = pyfits.open(file_path)
    fits_file_data = fits_file_list[1].data
    print '\n'
    print 'Catalog Loaded with ' + str(len(fits_file_data)) + '  Objects'
    return fits_file_data

