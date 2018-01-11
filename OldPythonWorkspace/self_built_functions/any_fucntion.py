# Purpose: TO Make a function that can be passed to another program to integrate
# or whatever you want to do with it.

import numpy as np
import pickle

magnitude_range = np.arange(0, 30, 0.25)
n_glob = 55000
sigma = 23.74
mew = 1.44

function = n_glob*