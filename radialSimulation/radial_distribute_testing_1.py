#! /usr/bin/python2.7

import random
import numpy as np
import sys
sys.path.append('/home/rlego/Documents/PythonWorkspace')
from any_func import *




range_limit = 200
samples = 200
step_size = 0.01

    
radialChoices = np.arange(0, range_limit, step_size)
    
radialDistributionValues = map(any_func, radialChoices)
theSum = sum(radialDistributionValues)
nSamples = 0
#NormalizedRadialDistributionValues = map(lambda x:x/float(theSum), radialDistributionValues)

sampledRadialValues = []
sampledAngularValues = [] 
    
while nSamples < 200:
            #this is sampling which radius
    tempRadiusRandom = random.sample(radialDistributionValues, 1)
            #this is sampling whether or not to use this number or not.
    tempCheckInside = random.uniform(0, max(radialDistributionValues))
        
    while tempCheckInside > any_func(tempRadiusRandom[0]):
                 #this is sampling which radius
        tempRadiusRandom = random.sample(radialDistributionValues, 1)
            #this is sampling whether or not to use this number or not.
        tempCheckInside = random.uniform(0, max(radialDistributionValues))
    sampledRadialValues.append(tempRadiusRandom[0])
    sampledAngularValues.append(random.uniform(0, 2*np.pi))
    nSamples = nSamples + 1
    print nSamples
        

       
xPosition = []
yPosition = []

for n in range(0, nSamples):
    xPosition.append(sampledRadialValues[n]*np.cos(sampledAngularValues[n]))
    yPosition.append(sampledRadialValues[n]*np.sin(sampledAngularValues[n]))
 #Now for plottiong the data
import matplotlib.pylab as plt

plt.scatter(xPosition, yPosition)
plt.show()
            
            
            
            
            
        
        
        
        