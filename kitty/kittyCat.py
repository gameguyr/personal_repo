#! /usr/bin/python2.7

#####################
# PURPOSE:to search for youtube videos of cats
#
# DATE:6/4/2013
#
# AUTHOR: Russell Lego
####################
import gdata
import gdata.youtube
import gdata.youtube.service


import gdata.youtube.service

def PrintEntryDetails(entry):

    print 'Video title: %s' % entry.media.title.text
    print 'Video published on: %s ' % entry.published.text
    print 'Video description: %s' % entry.media.description.text
    print 'Video category: %s' % entry.media.category[0].text
    if entry.media.keywords :
        print 'Video tags: %s' % entry.media.keywords.text
    #print 'Video watch page: %s' % entry.media.player.url
    print 'Video flash player URL: %s' % entry.GetSwfUrl()
    print 'Video duration: %s' % entry.media.duration.seconds

    # non entry.media attributes        
    if entry.geo :    
        print 'Video geo location: %s' % entry.geo.location

    # For video statistics
    if entry.statistics :       
        print 'Video view count: %s' % entry.statistics.view_count

    # For video rating
    if entry.rating  :    
        print 'Video rating: %s' % entry.rating.average

    # show alternate formats
    for alternate_format in entry.media.content:
        if 'isDefault' not in alternate_format.extension_attributes:
            print 'Alternate format: %s | url: %s ' % (alternate_format.type,
                                                     alternate_format.url)
    # show thumbnails
    for thumbnail in entry.media.thumbnail:
        print 'Thumbnail url: %s' % thumbnail.url
        
def PrintVideoFeed(feed):
    counter = 0
    for entry in feed.entry:
        PrintEntryDetails(entry)

def SearchAndPrint(search_terms):
  yt_service = gdata.youtube.service.YouTubeService()
  query = gdata.youtube.service.YouTubeVideoQuery()
  query.vq = search_terms
  query.orderby = 'viewCount'
  query.racy = 'include'
  feed = yt_service.YouTubeQuery(query)
  PrintVideoFeed(feed)
