#! /usr/bin/python2.7

#####################
# PURPOSE: to build the kitty catopia website backend database
#
# DATE: 8/1/2013
#
# AUTHOR: Russell Lego
####################

import gdata.youtube.service
import numpy as np
import pdb
import os
import json
import xlwt


## the list i'm using is 
##   list= ['crazy cats', 'funny cats', 'box cats', 'shaved cats', 'fat cats', 'big cats']
def dictBuilder(searchList):
    '''To give a list of categories you want to search for and to have 
        a json file pumped out,  ex:   dictBuilder(['funny cats', 'big cats'''
                                                    
    masterDict={}
    for search in searchList:
        
        yt_service = gdata.youtube.service.YouTubeService()
        query = gdata.youtube.service.YouTubeVideoQuery()
        print ''
        query.vq = search
        print''
        query.orderby = 'viewCount'
        query.racy = 'include'
        query.max_results = 50
        feed = yt_service.YouTubeQuery(query)
        pdb.set_trace()
        dict={}
        
        videoUrlList = []
        thumbnailUrlList = []
        descriptionList = []
        titleList = []

        for entry in feed.entry:
            videoUrlList.append(entry.GetSwfUrl())
            thumbnailUrlList.append(entry.media.thumbnail[0].url)
            descriptionList.append(entry.media.description.text)
            titleList.append(entry.media.title.text)
            dict['videoUrl']=videoUrlList
            dict['thumbnailUrl']=thumbnailUrlList
            dict['description']=descriptionList
            dict['title']=titleList
        print search+'  search completed'
        masterDict[search]=dict
        
#    fname='/Users/rlego/Dropbox/PythonWorkspace/masterDict.json'
    
    fname=raw_input('Enter the full path where you want the dictionary')
    file=open(fname, 'w')
    json.dump(masterDict, file, sort_keys=True, indent=4, separators=(',', ':'))
    file.close()
        
    print 'the program has completed'


def writeWorkbook(feed):
    excelWorkbook = xlwt.Workbook()
    sheet = excelWorkbook.add_sheet('Kitty Videos', cell_overwrite_ok=True)
    for i in range(0, np.size(feed.entry)):
        sheet.write(i, 0, '')
        sheet.write(i, 1, videoUrlList[i])
    path1 = os.getcwd()
    excelWorkbook.save(path1+'/'+raw_input('enter the name for the file'))
    excelWorkbook.close()



