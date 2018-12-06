#!/usr/bin/python
########################
# TITLE: u-g_vs_i-z
# AUTHOR: russell lego
# DATE: 2018-11-01
# PURPOSE:
########################


#################################
# Importing Modules
#################################
import pandas
import matplotlib.pyplot as plt
import numpy

#################################
# Defining Constants
#################################

file_path = '/Users/lego/Dropbox/Research/thesis/Working Thesis 2018-01-02/astronomy_data/MyTable_gameguyr.csv'


#################################
# Performing Work
#################################

df = pandas.read_csv(file_path)
u = numpy.array(df['modelMag_u'])
g = numpy.array(df['modelMag_g'])
i = numpy.array(df['modelMag_i'])
z = numpy.array(df['modelMag_z'])
plt.scatter(u-g, i-z,  marker='.', s=0.1)

xmin = -14
xmax = 14
ymin = -14
ymax = 14
plt.xlim( (xmin, xmax) )
plt.ylim( (ymin, ymax) )


plt.xlabel('i-z')
plt.ylabel('u-g')
plt.title('U-G vs. I-Z')
plt.show()