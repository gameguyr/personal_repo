import urllib
import urllib2
from bs4 import BeautifulSoup

#Enter the URL

page = 'http://surveys.roe.ac.uk:8080/wsa/WSASQL'

#Creating the inputs for the Form Submission
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
w1_path = '/Users/rlego/PythonWorkspace/posting/test_write_3.txt'
f3 = open(w1_path, 'w')


#creating the arrary containg the coordinates for input
sql_input=[]

for i in range(len(coord)-1):
    sql_input.append(s1+coord[i]+s2)

sql_alt=sql_input[1014:]
index=[]

for i in range(len(sql_input)-1): 
    inputs={'formaction':'freeform','database':'UKIDSSDR8PLUS',\
            'sqlstmt':sql_input[i],'emailAddress':'gameguyr@gmail.com',\
             'format':'FITS','compress':'NONE','rows':'30','timeout':'100000'}
    encodedInputs = urllib.urlencode(inputs)
    request = urllib2.Request(page, encodedInputs)
    fConnection = urllib2.urlopen(request)
    returnedHTML = fConnection.read()
    soup = BeautifulSoup(returnedHTML)
    url4fits = soup.a['href']
    index4fits = url4fits.find('results')
    fits = url4fits[index4fits:]
    urllib.urlretrieve(url4fits, fits)
    print i
    string = str(i)
    index.append(i)
    f3.writelines(string + ' ')
    

print index   
f3.close()
