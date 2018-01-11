import urllib
import urllib2
from bs4 import BeautifulSoup

#Enter the URL

page = 'http://surveys.roe.ac.uk:8080/wsa/WSASQL'

#Creating the inputs for the Form Submission
# gobble_one.txt i the file containing all the coordinates
file_path = '/Users/rlego/PythonWorkspace/posting/gobble_one.txt'
file = open(file_path, 'r')
coord= file.readlines()
file.close()

s_path1 = '/Users/rlego/PythonWorkspace/posting/sql_pt1.txt'
s_path2 = '/Users/rlego/PythonWorkspace/posting/sql_pt2.txt'
f1 = open(s_path1,'r')
f2 = open(s_path2,'r')
s1 = f1.read()
s2 = f2.read()
f1.close
f2.close

#creating the arrary containg the coordinates for input
sql_input=[]

for i in range(len(coord)-1):
    sql_input.append(s1+coord[i]+s2)

sql_alt=sql_input[5814]

inputs={'formaction':'freeform','database':'UKIDSSDR8PLUS',\
        'sqlstmt':sql_alt,'emailAddress':'gameguyr@gmail.com',\
        'format':'FITS','compress':'NONE','rows':'30','timeout':'3600'}
encodedInputs = urllib.urlencode(inputs)
request = urllib2.Request(page, encodedInputs)
fConnection = urllib2.urlopen(request)
returnedHTML = fConnection.read()
soup = BeautifulSoup(returnedHTML)
url4fits = soup.a['href']
index4fits = url4fits.find('results')
fits = url4fits[index4fits:]
urllib.urlretrieve(url4fits, fits)