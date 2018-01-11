# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:51:52 2012

@author: therese
"""

#!/usr/bin/python

def fib(n):
    print n
    if n < 2:
        return 1
        
    else:
        return fib(n-1) + fib(n-2)
    


fib(150000)