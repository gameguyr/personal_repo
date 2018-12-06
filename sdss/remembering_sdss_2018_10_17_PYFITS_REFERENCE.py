#!/usr/bin/python
########################
# TITLE: remembering_sdss_2018_10_17
# AUTHOR: russell lego
# DATE: 2018-10-17
# PURPOSE: trying to manipulate the fits file using the examples on the website.
# http://docs.astropy.org/en/stable/io/fits/#f1
#
# The goal of this is to plot the number of objects as I decrease the magnitude.
# to show that the number of objects is highly dependent on the magnitude
########################


from astropy.io import fits
import numpy
import matplotlib.pyplot as plt
import numpy as np




fits_image_filename = '/Users/lego/Dropbox/Research/thesis/Working Thesis 2018-01-02/astronomy_data/sdss_2016_01_13.fit'

header_data_unit_list = fits.open(fits_image_filename)
header_data_unit_table = header_data_unit_list[1]
header_data_unit_table_data = header_data_unit_table.data

# here's how to get all the columns of the data table
columns_list = header_data_unit_table.columns.names

# header_data_unit_list.info()


# now getting the arrays to plot

number_of_objects = []


modelMag_u_max = max(header_data_unit_table_data['modelMag_u'])
modelMag_u_min = min(header_data_unit_table_data['modelMag_u'])

interval_of_magnitude = numpy.arange(modelMag_u_min, modelMag_u_max, 0.1)





for i in range(0, len(interval_of_magnitude)):
    index_where_modelMag_u_is_below = numpy.where(header_data_unit_table_data['modelMag_u'] < interval_of_magnitude[i])
    number_of_objects.append(len(header_data_unit_table_data['modelMag_u'][index_where_modelMag_u_is_below]))

# now I am going to plot the array of data that I have created.

# plt.scatter(interval_of_magnitude, number_of_objects,  marker='o', s=0.3)
# plt.xlabel('interval_of_magnitude')
# plt.ylabel('number_of_objects')
# plt.title('number_of_objects vs. interval_of_magnitude')
# plt.show()


# I am trying to get the histogrtam values
histograms_values, bins = numpy.histogram(a, bins = [0,20,40,60,80,100])

# plt.scatter(interval_of_magnitude, number_of_objects,  marker='o', s=0.3)
# plt.xlabel('interval_of_magnitude')
# plt.ylabel('number_of_objects')
# plt.title('number_of_objects vs. interval_of_magnitude')
# plt.show()

