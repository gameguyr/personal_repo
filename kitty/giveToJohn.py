#! /usr/bin/python2.7

#####################
# PURPOSE: to give John Crain the kpw database
#
# DATE: 8/2/2013
#
# AUTHOR: Russell Lego
####################

import pdb
import pickle
fname = raw_input('Please give the FULL path to the kitty data file    ')
file = open(fname, 'r')
dataBase = pickle.load(file)

print '''

The database is a collection urls and text for the videos, thumbnails, 
titles, and desciptions for each video

There are 4 keys in this dictionary (videoUrl, thumbnailUrl, 
title, and desciption) each of which has a value that is an array of 
whatever that key is describing.
'''
print'''

example1:

dataBase['videoUrl']

this will give you a list of all the url's for the videos in the database

example2:

dataBase['thumbnailUrl']

this will give you a list of all the url's for the thumbnails for each video
 in the database

'''

pdb.set_trace()