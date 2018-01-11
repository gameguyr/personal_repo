import os, glob

path = "./"
fileList = os.listdir(path)

for eachFile in fileList:
    print str(fileList.index(eachFile)) +" : " + eachFile
