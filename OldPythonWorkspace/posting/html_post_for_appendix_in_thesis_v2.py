#!/usr/bin/python
########################
# TITLE: html_post_for_appendix_in_thesis_v2.py
# AUTHOR: russell lego
# DATE: 2019-02-06
# PURPOSE: to get a version of the posting example to put in my thesis in the appendix
########################


#################################
# Importing Modules
#################################
import urllib
import urllib2
from bs4 import BeautifulSoup

#################################
# Defining Constants
#################################
url_for_wsa_server = 'http://surveys.roe.ac.uk:8080/wsa/WSASQL'

sql_query_part_1 = '''SELECT
   las.ra,
   las.dec,
   las.pGalaxy,
   las.pStar,
   las.yAperMag3,
   las.yAperMag3Err,
   las.j_1AperMag3,
   las.j_1AperMag3Err,
   las.hAperMag3,
   las.hAperMag3Err,
   las.kAperMag3,
   las.kAperMag3Err,
   las.yppErrBits,
   las.j_1ppErrBits,
   las.hppErrBits,
   las.kppErrBits,
   pho.OBJID
FROM
   lasSource AS las,
   BestDR7..PhotoObj AS pho
   left outer join
      BestDR7..specObj AS spec
      on pho.ObjID = spec.BestObjID,
      lasSourceXDR7PhotoObj AS x
WHERE
   masterObjID = las.sourceID
   AND slaveObjID = pho.ObjID
   AND distanceMins < 0.033333
   AND sdssPrimary = 1
   AND
   (
'''

sql_query_part_2 = '''   )
   AND distanceMins IN 
   (
      SELECT
         MIN(distanceMins) 
      FROM
         lasSourceXDR7PhotoObj 
      WHERE
         masterObjID = x.masterObjID 
         AND sdssPrimary = 1
   )'''

coordinate_file_path = 'gobble_one.txt'
coordinate_file_object = open(coordinate_file_path, 'r')
coordinate_array = coordinate_file_object.readlines()
coordinate_file_object.close()
#################################
# Performing Work
#################################

sql_query_array=[]

for i in range(0, len(coordinate_array)):
    sql_query_array.append(sql_query_part_1 + coordinate_array[i] + sql_query_part_2)

for j in range(0, len(sql_query_array)):
    print '*' * 50
    print 'Here is the query for batch # : {0}'.format(str(j))
    print '*' * 50
    print sql_query_array[j]
    print '*' * 50
    inputs={'formaction':'freeform','database':'UKIDSSDR8PLUS',\
            'sqlstmt':sql_query_array[j],'emailAddress':'gameguyr@gmail.com',\
            'format':'FITS','compress':'NONE','rows':'30','timeout':'3600'}
    encodedInputs = urllib.urlencode(inputs)
    request = urllib2.Request(url_for_wsa_server, encodedInputs)
    fConnection = urllib2.urlopen(request)
    returnedHTML = fConnection.read()
    soup = BeautifulSoup(returnedHTML)
    url4fits = soup.a['href']
    index4fits = url4fits.find('results')
    fits = url4fits[index4fits:]
    urllib.urlretrieve(url4fits, fits)