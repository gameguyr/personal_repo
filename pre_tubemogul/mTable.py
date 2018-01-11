#!/Users/rlego/anaconda/bin/python
# trying to solve some sample programming questions
# this one is for a multiplication table
import numpy as np


def mTable(x, y):
    array = np.zeros((x+1, y+1), dtype=np.int)
    rows = np.arange(0, x+1)
    cols= np.arange(0, y+1)
    
    for col in cols:
        for row in rows:
            if col==0:
                array[row, col]=(col+1)*row
            elif row==0:
                array[row, col]=(col)*(row+1)
            else:
                array[row, col] = row*col
            
    print array