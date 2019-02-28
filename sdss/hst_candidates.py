#!/usr/bin/python
########################
# TITLE: hst_candidates
# AUTHOR: russell lego
# DATE: 2019-02-27
# PURPOSE:TO extract the images of the objects within the HstCandidates.fits
# I basically need to get the images of them so that I could put them as examples
# of what I was looking for in my thesis.
########################


#################################
# Importing Modules
#################################
import sdss_common

#################################
# Defining Constants
#################################
file_path = 'HstCandidates.fits'
sdss_obj_tool_url = 'http://skyserver.sdss.org/dr7/en/tools/explore/obj.asp?id='

#################################
# Defining Functions
#################################


#################################
# Defining Classes
#################################


#################################
# Performing Work
#################################

hst_catalog_object = sdss_common.load_fits_file(file_path)
for astro_object in hst_catalog_object:
    print sdss_obj_tool_url + str(astro_object[0])


