#!/usr/bin/python
########################
# TITLE: rotate
# AUTHOR: russell lego
# DATE: 2018-08-20
# Check out the resources on the page's right side to learn more about arrays. The video tutorial is by Gayle Laakmann McDowell, author of the best-selling interview book Cracking the Coding Interview.
#
# A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become .
#
# Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.
#
# Function Description
#
# Complete the function rotLeft in the editor below. It should return the resulting array of integers.
#
# rotLeft has the following parameter(s):
#
# An array of integers .
# An integer , the number of rotations.
# Input Format
#
# The first line contains two space-separated integers  and , the size of  and the number of left rotations you must perform.
# The second line contains  space-separated integers .
########################

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.

def rotLeft(a, d):

    for i in range(0, d):
        a.append(a.pop(0))
        return a


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)

    print ' '.join(map(str, result))


