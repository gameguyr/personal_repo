#!/usr/bin/python
########################
# TITLE: plotting_HR_diagram_from_sdss_v1
# AUTHOR: russell lego
# DATE: 2018-09-19
# PURPOSE: to plot g-r vs r from tje sdss.  I have downloaded a substantial size of data from the sdss
# and now I am refreshing my mind on getting used to the data.
########################


#################################
# Importing Modules
#################################
import matplotlib.pyplot as plt
import numpy as np

#################################
# Defining Constants
#################################


#################################
# Defining Functions
#################################


#################################
# Defining Classes
#################################


#################################
# Performing Work
#################################




#############################
##  loading data
#############################
file_name = 'g-r_vs_r_sdss_v1.csv'
data = np.loadtxt(file_name, skiprows = 1, unpack = True, delimiter = ',')


magnitude = data[0]
color = data[1]




#############################
##  setting plot parameters
#############################
# plt.plot(color, magnitude, marker ='o', linestyle ='none')
plt.scatter(color, magnitude,  marker='.', s=0.1)


# xmin = 0
# xmax = 100
# ymin = 0
# ymax = 50000000
plt.xlabel('g-r')
plt.ylabel('r')
plt.title('r vs. g-r')
# plt.xlim( (xmin, xmax) )
# plt.ylim( (ymin, ymax) )



#############################
##  plotting and saving image
#############################
# plt.grid(True)
# plt.savefig("test.png")
plt.show()



#############################