import urllib
import urllib2
from bs4 import BeautifulSoup

page = 'http://surveys.roe.ac.uk:8080/wsa/WSASQL'

inputs={'formaction':'freeform',
             'database':'UKIDSSDR2PLUS',
             'sqlstmt':'select top 10 sourceID from lasSource',
             'emailAddress':'gameguyr@gmail.com',
             'format':'FITS',
             'compress':'NONE',
             'rows':'30',
             'timeout':'3600'}

encodedInputs = urllib.urlencode(inputs)

request = urllib2.Request(page, encodedInputs)

fConnection = urllib2.urlopen(request)

returnedHTML = fConnection.read()

soup=BeautifulSoup(returnedHTML)
url4fits=soup.a['href']
fits=url4fits[-26]
urllib.urlretrieve(url4fits, fits)