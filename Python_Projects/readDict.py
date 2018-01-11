#!/usr/bin/python

mydict = []
tempDict = dict()
f = "dictTest.txt"
fr = open(f)
temp = fr.readlines()
for line in temp:
  line.replace(" ", "")
  tempDict = {}
  try:
    dic = eval(line)
    for x,v in dic.iteritems():
      tempDict[x]=v
  except:
    "In except"
  mydict.append(tempDict)
  continue
fr.close()
print mydict
person2 = {'city': 'Morocco', 'last': 'Blah', 'phone': '415 777 4434', 'state': 'MO', 'street': '1 Boondocks St.', 'email': 'dud@yahoo.com', 'first': 'Joe'}
f2 = open(f, "a+")
f2.write(str(person2))
f2.close()



