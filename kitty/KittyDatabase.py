#! /usr/bin/python2.7

#####################
# PURPOSE: to build the kitty catopia website backend database
#
# DATE: 8/1/2013
#
# AUTHOR: Russell Lego
####################

import gdata.youtube.service
import numpy as np
import xlwt
import webbrowser
import pdb

yt_service = gdata.youtube.service.YouTubeService()
query = gdata.youtube.service.YouTubeVideoQuery()
print ''
query.vq = raw_input('Please enter the desired search')
print''
query.orderby = 'viewCount'
query.racy = 'include'
query.max_results = 50
feed = yt_service.YouTubeQuery(query)
#  print np.size(feed.entry)
#  time.sleep(5.5)


#def dictionaryBuilder(feed):
#    tempDict={}
#    for items in feed.entry:



dictionary={}
for entry in feed.entry:
    dictionary['videoUrl']=entry.GetSwfUrl()
    dictionary['thumbnailUrl']=entry.media.thumbnail[0].url
    dictionary['description']=entry.media.description.text
    dictionary['title']=entry.media.title.text
    
    
pdb.set_trace()