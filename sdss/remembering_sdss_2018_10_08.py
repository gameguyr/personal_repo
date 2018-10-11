#!/usr/bin/python
########################
# TITLE: remebering_sdss_2018_10_08
# AUTHOR: russell lego
# DATE: 2018-10-10
# PURPOSE:
########################


#################################
# Importing Modules
#################################
import sdss_common
import astropy.io.fits as pyfits
#################################
# Defining Constants
#################################
file_path_for_catalog = 'sdss_2016_01_13.fit'

#################################
# Defining Functions
#################################


#################################
# Defining Classes
#################################


#################################
# Performing Work
#################################

# catalog_data = sdss_common.load_fits_file(file_path_for_catalog)
#
# print catalog_data[1]

# pyfits.info(file_path_for_catalog)
catalog_header = pyfits.getheader(file_path_for_catalog)
print catalog_header