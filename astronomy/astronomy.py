#! /usr/bin/python2.7

#####################
# PURPOSE: to confirm the UCD target at KPNO the sombrero one
#
# DATE: 
#
# AUTHOR: Russell Lego
####################


import numpy as np
import sys

def hms2dec(h,m,s):
    hours = float(h)+float(m)/60.+float(s)/3600.
    dec = hours*180./12.
    return dec

def dms2deg(d,m,s):
    deg = float(d)+float(m)/60.+float(s)/3600.
    return deg

def deg2hms(deg):
     x = deg*(24./360.)
     h = int(x)
     y = x % h * 60.
     m = int(y)
     s = y % m * 60
     return h,m,s

def deg2dms(deg):
     d = int(deg)
     y = deg % d * 60.
     m = int(y)
     s = y % m * 60
     return d,m,s


ra_h = 12
ra_m = 44
ra_s = 17.83

dec_d = 11
dec_m = 27
dec_s = 42.8
print 'going from:   ' + str(ra_h) + ':' + str(ra_m) + ':' + str(ra_s) + '    to:   ' + str(hms2dec(ra_h, ra_m, ra_s))
print 'going from:   ' + str(dec_d) + ':' + str(dec_m) + ':' + str(dec_s) + '    to:   ' + str(dms2deg(dec_d, dec_m, dec_s))