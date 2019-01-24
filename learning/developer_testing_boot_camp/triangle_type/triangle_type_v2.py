#!/usr/bin/python
########################
# TITLE: triangle_type_v2
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
    if a + b <= c or b + c <= a or a + c <= b:
        return 'INVALID'
    if a == b and b == c:
        return 'EQUILATERAL'
    elif a == b or b == c or c == a:
        return 'ISOSCELES'
    else:
        return 'SCALENE'

class TriangleTest(unittest.TestCase):

    def test_is_valid_scalene(self):
        a = 3
        b = 4
        c = 5
        self.assertEqual(classify(a, b, c), 'SCALENE')

    def test_is_valid_equilateral(self):
        a = 3
        b = 3
        c = 3
        self.assertEqual(classify(a, b, c), 'EQUILATERAL')

    def test_is_valid_isosceles(self):
        a = 3
        b = 3
        c = 1
        self.assertEqual(classify(a, b, c), 'ISOSCELES')
        self.assertEqual(classify(a, c, b), 'ISOSCELES')
        self.assertEqual(classify(b, c, a), 'ISOSCELES')
        self.assertEqual(classify(b, a, c), 'ISOSCELES')
        self.assertEqual(classify(c, a, b), 'ISOSCELES')
        self.assertEqual(classify(c, b, a), 'ISOSCELES')


    def test_is_invalid_for_zero_length(self):
        a = 3
        b = 3
        c = 0
        self.assertEqual(classify(a, b, c), 'INVALID')

    def test_is_invalid_for_negative_length(self):
        a = 3
        b = 3
        c = -1
        self.assertEqual(classify(a, b, c), 'INVALID')

    def test_is_invalid_for_two_sides_equal_to_third(self):
        a = 1
        b = 2
        c = 3
        self.assertEqual(classify(a, b, c), 'INVALID')
        self.assertEqual(classify(a, c, b), 'INVALID')
        self.assertEqual(classify(b, c, a), 'INVALID')
        self.assertEqual(classify(b, a, c), 'INVALID')
        self.assertEqual(classify(c, a, b), 'INVALID')
        self.assertEqual(classify(c, b, a), 'INVALID')

    def test_is_invalid_for_sum_of_two_sides_is_less_than_third(self):
        a = 12
        b = 15
        c = 30
        self.assertEqual(classify(a, b, c), 'INVALID')
        self.assertEqual(classify(a, c, b), 'INVALID')
        self.assertEqual(classify(b, c, a), 'INVALID')
        self.assertEqual(classify(b, a, c), 'INVALID')
        self.assertEqual(classify(c, a, b), 'INVALID')
        self.assertEqual(classify(c, b, a), 'INVALID')

    def test_is_invalid_for_all_sides_zero(self):
        a = 0
        b = 0
        c = 0
        self.assertEqual(classify(a, b, c), 'INVALID')
        self.assertEqual(classify(a, c, b), 'INVALID')
        self.assertEqual(classify(b, c, a), 'INVALID')
        self.assertEqual(classify(b, a, c), 'INVALID')
        self.assertEqual(classify(c, a, b), 'INVALID')
        self.assertEqual(classify(c, b, a), 'INVALID')