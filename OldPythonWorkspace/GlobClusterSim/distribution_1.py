#
# Purpose:
# To Create a monte Carlo simulation for the distribution of Globular CLusters around M87

from numpy import *

n_theta = 100
r_theta = [0, 2*pi]  # angular range
h_theta = (r_theta[1]-r_theta[0])/(n_theta-1)
theta = arange(0, 2*pi, h_theta)
angular_slices = size(theta)
n_glob = 55000

print
#print 'this is how big theta  is', size(theta)
print

n_radius = 10001.
r_radius = [0, 200]  #range in kilo-parsecs
h_radius = (r_radius[1]-r_radius[0])/(n_radius-1)

radius = arange(r_radius[0], r_radius[1], h_radius)

radial_function = (n_glob/angular_slices)/(radius**2+1)

radius_sample =random.sample(radial_function)
#for i in range(0, angular_slices):
    

positions = {'x_position':zeros(n_glob), 
'y_position':zeros(n_glob),'z_position':zeros(n_glob)}