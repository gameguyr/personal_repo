# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:30:17 2013

@author: rlego
"""
#PURPOSE: 
#to convert decimal degrees to DMS

def decdeg2dms(dd):
    mnt,sec = divmod(dd*3600,60)
    deg,mnt = divmod(mnt,60)
    return deg,mnt,sec
#def dms2decdeg(h,m,s):
    