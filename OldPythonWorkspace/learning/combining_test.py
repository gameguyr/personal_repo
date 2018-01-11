#!/user/bin/python

path='/Users/rlego/PythonWorkspace/posting/gobble.txt'
file=open(path, 'r')
c_split=file.readlines()
c_join=[]

for i in range(len(c_split)-1):
    c_join.append(c_split[i]+c_split[i+1])
print c_join[0], c_join[-1]
