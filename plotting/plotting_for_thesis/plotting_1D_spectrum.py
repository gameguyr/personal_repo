#!/usr/bin/python
########################
# TITLE: plotting_1D_spectrum
# AUTHOR: russell lego
# DATE: 2019-05-26
# PURPOSE: I was trying to plot the overscan region of the flat field image.
# I could see that the ccdproc actually trimmed off the arrays though. No way to get it back.
# EDIT
# I actually found the RAW FLAT FILES AND THEY DO HAVE THE EXTRA BITS PAST 2046
########################


#################################
# Importing Modules
#################################
import pyfits
import matplotlib.pyplot as plt
#################################
# Defining Constants
#################################
file_path = '/Users/lego/Dropbox/College/Research/KPNO_copy/flat/raw/a0008.fits'

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

line_to_plot = fits_file_data[258]
x_axis_for_plot = range(0, len(line_to_plot))







#############################
##  plotting and saving image
#############################
# plt.scatter(x_axis_for_plot, line_to_plot,  marker='.', s=0.1)

plt.plot(x_axis_for_plot, line_to_plot, color = 'black')
xmax = 2100
xmin = 2000
ymin = 0
ymax = 10000
plt.xlabel('Column')
plt.ylabel('ADU')
plt.title('Counts vs. Column  (Overscan Region in Flat Field Image)')
plt.xlim( (xmin, xmax) )
plt.ylim( (ymin, ymax) )
# plt.grid(True)
# plt.savefig("test.png")
plt.show()