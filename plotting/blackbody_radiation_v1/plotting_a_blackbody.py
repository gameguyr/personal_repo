#!/usr/bin/python
# coding=utf-8
########################
# TITLE: plotting_a_blackbody
# AUTHOR: russell lego
# DATE: 2018-12-05
# PURPOSE:
########################


#################################
# Importing Modules
#################################
import numpy
import matplotlib.pyplot as plot
import matplotlib


#################################
# Defining Constants
#################################
colors_array = matplotlib.colors.cnames.keys()

## physics constants
h  = 6.626e-34
b  = 2.897e-3
kB = 1.380e-23
# sigma = 5.670373 * 10**-8
c  = 299792458.0

## sdss bands
u_band = 3543e-10
g_band = 4770e-10
r_band = 6231e-10
i_band = 7625e-10
z_band = 9134e-10

## defining discretization

lamda_start = 20*10**-10
lamda_end = 50000*10**-10
T = 5000
temperature_array = numpy.arange(2000, 20000, 1000)
lamda_array = numpy.arange(lamda_start, lamda_end, 1*10**-10)

################################
# Defining Functions
#################################
def therm_radiation_power(input_lamda_array, temp):
    output_therm_radiation_power_array = numpy.zeros(len(input_lamda_array))

    for i in range(0, len(input_lamda_array)):
        output_therm_radiation_power_array[i] = (2 * h * c**2 / input_lamda_array[i]**5) * ( 1 / (numpy.e**(h*c/(kB*temp*input_lamda_array[i])) -1 ))

    return output_therm_radiation_power_array

def therm_radiation_power_array_operation(input_lamda_array, temp):

    output_therm_radiation_power_array = (2 * h * c**2 / input_lamda_array**5) * ( 1 / (numpy.e**(h*c/(kB*temp*input_lamda_array)) -1 ))

    return output_therm_radiation_power_array




#################################
# Performing Work
#################################
plot.hold(True)
for i in range(0, len(temperature_array)):
    color_marker_index = numpy.random.randint(0, len(colors_array))
    plot.scatter(lamda_array, therm_radiation_power_array_operation(lamda_array, temperature_array[i]), marker='.', s=0.1, c=colors_array[color_marker_index])
plot.xlabel('lamda_array')
plot.ylabel('therm_radiation_power')
xmin = lamda_start
xmax = lamda_end

plot.xlim( (-1e-6, xmax) )
# plot.ylim( (ymin, ymax) )
plot.show()