# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 01:34:00 2013

@author: rlego
"""
#PURPOSE: 
#
#to understand how to run code faster with efficient array operations
import numpy as np

x=np.arange(1500)


for item1 in x:
    for item2 in x[:-1]:
        print item-item2
        
        