#!/user/bin/python
import sys


ra=['balls', 'sweat', 'smells', 'funky']
r=[]
for i, ele in range(len(ra)-1):
#    print "myElement ", ele, " at index: ",i
    r.append(ra[i]+ra[i+1])
print r
