#! /usr/bin/python2.7

#####################
# PURPOSE: to get things from the internet atuo style
#
# DATE:4/29/2013
#
# AUTHOR: Russell Lego
####################

import bs4
import urllib as u1
import urllib2 as u2
from bs4 import BeautifulSoup as bs


object = 'm60'
page1 = 'http://ned.ipac.caltech.edu/cgi-bin/objsearch?objname='
page2 = '&extend=no&hconst=73&omegam=0.27&omegav=0.73&corr_z=1&out_csys=Equatorial&out_equinox=J2000.0&obj_sort=RA+or+Longitude&of=pre_text&zv_breaker=30000.0&list_limit=5&img_stamp=YES'

inputs={'submit':'Submit Query', 'objname':'m60'}

encodedInputs = u1.urlencode(inputs)
request = u2.Request(page, encodedInputs)
fConnection = u2.urlopen(request)
returnedHTML = fConnection.read()
soup = bs(returnedHTML)

