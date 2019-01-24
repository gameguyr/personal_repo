#!/usr/bin/python
########################
# TITLE: triangle_type
# AUTHOR: russell lego
# DATE: 2018-12-13
# PURPOSE:
########################


#################################
# Importing Modules
#################################

import unittest
#################################
# Defining Constants
#################################


#################################
# Defining Functions
#################################


#################################
# Defining Classes
#################################


#################################
# Performing Work
#################################

def classify(a, b, c):
    if (a + b <= c or b + c <= a or a + c <= b):
        return 'INVALID'
    if (a == b and b == c):
        return 'EQUILATERAL'
    elif (a == b or b == c or c == a):
        return 'ISOSCELES'
    else:
        return 'SCALENE'

class IsValidScaleneTriangle(unittest.TestCase):

    def test_is_valid(self):
        a = 3
        b = 4
        c = 5
        self.assertEqual(classify(a, b, c), 'SCALENE')