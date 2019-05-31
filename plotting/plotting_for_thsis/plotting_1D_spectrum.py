#!/usr/bin/python
########################
# TITLE: plotting_1D_spectrum
# AUTHOR: russell lego
# DATE: 2019-05-26
# PURPOSE:
########################


#################################
# Importing Modules
#################################
import pyfits
import matplotlib.pyplot as plt
#################################
# Defining Constants
#################################
file_path = '/Users/lego/Dropbox/College/Research/KPNO_copy/sombreroCombined.ms.fits'

#################################
# Defining Functions
#################################


#################################
# Defining Classes
#################################


#################################
# Performing Work
#################################

fits_file_list = pyfits.open(file_path)
fits_file_data = fits_file_list[0].data

band_0 = fits_file_data[0][0]
band_1 = fits_file_data[1][0]
band_2 = fits_file_data[2][0]
band_3 = fits_file_data[3][0]






#############################
##  plotting and saving image
#############################
plt.scatter(band_2, band_0,  marker='.', s=0.1)
xmin = 3000
xmax = 9000
# ymin = 0
# ymax = 50000000
plt.xlabel('wavelength')
plt.ylabel('ADU')
# plt.title('r vs. g-r')
# plt.xlim( (xmin, xmax) )
# plt.ylim( (ymin, ymax) )
# plt.grid(True)
# plt.savefig("test.png")
plt.show()