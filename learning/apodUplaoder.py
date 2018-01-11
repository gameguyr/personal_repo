#! /usr/bin/python2.7

#####################
# PURPOSE: to upload the astronomy picture of the day to my desktop
#
# DATE: 6/12/2013
#
# AUTHOR: Russell Lego
####################




import appscript
import urllib
import urllib2
appscript.app('Finder').desktop_picture.set(appscript.mactypes.File('/your/filename.jpg'))




####################
# DOwnloading the picture
####################

page1stHalf = 'http://apod.nasa.gov/apod/'
page2ndHalf = '.html'

page = 'http://apod.nasa.gov/apod/ap130515.html'


fConnection = urllib2.urlopen(page)
returnedHTML = fConnection.read()
soup = BeautifulSoup(returnedHTML)
imageUrl = soup.br['href']
#index4fits = url4fits.find('results')
#fits = url4fits[index4fits:]
urllib.urlretrieve(url4fits, fits)