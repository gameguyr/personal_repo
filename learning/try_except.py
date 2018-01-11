
#! /Users/rlego/anaconda/bin/python

#####################
# PURPOSE: to learn the uses of try and except		
#
# DATE: Sun Sep 28 12:50:58 PDT 2014
#
# AUTHOR: Russell Lego
####################

try:
	import mysqlcl
	check =True
except ImportError:
	print "no mysqlcl avilable"
	check=False

print check