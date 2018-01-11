# Purpose:  To ceate a program to numerically integrate functions
# using the Simpson method

import numpy as np
big_n = 2E20+1
h = (range[1]-range[0])/(big_n-1)
X = (DINDGEN(big_n)*h)+range[0]        
Y = any_func(x) 


###############################################
#    Calculating the Integral using Simpson's
###############################################


index = DINDGEN(N_ELEMENTS(Y[1:big_n-2]))+1
Y_index = Y[1:big_n-2]
even =  WHERE(2*(ROUND(index)/2) EQ index)
odd  =  WHERE(2*(ROUND(index)/2) NE index)

integral_simp = (h/3)*(4*TOTAL(Y_index[odd])+$
2*TOTAL(Y_index[even])+Y[0]+Y[big_n-1])