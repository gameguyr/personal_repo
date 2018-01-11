#! /usr/bin/python2.7

#####################
# PURPOSE: to change the background picture of my desktop
#
# DATE: 8/20/2013
#
# AUTHOR: Russell Lego
####################




import appscript
fname1='/Users/rlego/Desktop/'
fname2=raw_input('Enter the name of the file on the desktop:    ')
appscript.app('Finder').desktop_picture.set(appscript.mactypes.File(fname1+fname2))




