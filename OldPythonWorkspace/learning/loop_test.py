#!/user/bin/python


ra=['balls', 'sweat', 'smells', 'funky']
e=[]
r=[]

for i in range(len(ra)-1):
    #print ra[i]+ ra[i+1]
    e.append(ra[i]+ ra[i+1])
print e

for i in range(len(e)-1):
    r.append(e[2*i])
print r


#for i in ra:
#    print i, i[1]

