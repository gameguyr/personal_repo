#! /usr/bin/python2.7

#####################
# PURPOSE:to search for youtube videos of cats
#
# DATE:6/4/2013
#
# AUTHOR: Russell Lego
####################
import gdata
import gdata.youtube
import gdata.youtube.service
import Tkinter as tk
import tkMessageBox as mb
from Tkinter import Tk, W, E
from ttk import Frame, Button, Label, Style
from ttk import Entry
import time
import gdata.youtube.service
import numpy as np
import xlwt
import webbrowser
import os



########################################
#  Defining variables to store
#  for later usage
########################################

urlList = []
approvedUrlList = []
jpgList = []


excelWorkbook = xlwt.Workbook()
sheet = excelWorkbook.add_sheet('Kitty Videos', cell_overwrite_ok=True)

videoCounter = 0
########################################
#  Defining functions for buttons
########################################


def printEntryDetails(entry):
    print ''
    print '##################################'
    print ''
    print 'Video title: %s' % entry.media.title.text
    print 'Video published on: %s ' % entry.published.text
    print 'Video description: %s' % entry.media.description.text
    print 'Video category: %s' % entry.media.category[0].text
    if entry.media.keywords :
        print 'Video tags: %s' % entry.media.keywords.text
    #print 'Video watch page: %s' % entry.media.player.url
    print 'Video flash player URL: %s' % entry.GetSwfUrl()
    print 'Video duration: %s' % entry.media.duration.seconds
    
    # non entry.media attributes        
    if entry.geo :    
        print 'Video geo location: %s' % entry.geo.location

    # For video statistics
    if entry.statistics :       
        print 'Video view count: %s' % entry.statistics.view_count

    # For video rating
    if entry.rating  :    
        print 'Video rating: %s' % entry.rating.average

    # show alternate formats
    for alternate_format in entry.media.content:
        if 'isDefault' not in alternate_format.extension_attributes:
            print 'Alternate format: %s | url: %s ' % (alternate_format.type,
                                                     alternate_format.url)
    # show thumbnails
    for thumbnail in entry.media.thumbnail:
        print 'Thumbnail url: %s' % thumbnail.url
        
def printVideoFeed(feed):
    counter = 0
    for entry in feed.entry:
        printEntryDetails(entry)
        urlList.append(entry.GetSwfUrl())
        
def writeWorkbook(feed):
    for i in range(0, np.size(feed.entry)):
        sheet.write(i, 0, '')
        sheet.write(i, 1, urlList[i])
    path1 = os.getcwd()
    excelWorkbook.save(path1+'/'+raw_input('enter the name for the file'))
        

def searchAndPrint():
  yt_service = gdata.youtube.service.YouTubeService()
  query = gdata.youtube.service.YouTubeVideoQuery()
  query.vq = categoryEntry.get()
  if authorVar.get() == 1:
      query.author = authorEntry.get()
  query.orderby = 'viewCount'
  query.racy = 'include'
  query.max_results = 5
  feed = yt_service.YouTubeQuery(query)
#  print np.size(feed.entry)
#  time.sleep(5.5)
  printVideoFeed(feed)
  if excelVar.get() == 1:
    writeWorkbook(feed)
    
def displayPage():
    global videoCounter
    handle = webbrowser.get()
    handle.open_new_tab(urlList[videoCounter])
    videoCounter = videoCounter+1
    print 'the count is now', videoCounter
    
#def approval():
#    approvedUrlList.append(urlList[videoCounter])
#def disapproval():
    
  
#######################
# Tk part1   #
#######################


the_window = tk.Tk()
frame = Frame(the_window)
the_window.title('Kitty Cat Approval')
the_window.geometry('450x250+0+500')
      

Style().configure('TButton', padding=(0, 5, 0, 5), 
    font='serif 10')

frame.columnconfigure(0, pad=3)

frame.rowconfigure(0, pad=3)
#frame.rowconfigure(1, pad=3)
#frame.rowconfigure(2, pad=3)
#frame.rowconfigure(3, pad=3)
##  ENTRY  ###
categoryLabel = Label(frame, text='Category')
categoryLabel.grid(row=0, column=0)
categoryEntry = Entry(frame)
categoryEntry.grid(row=0, column=1)

 
timeLabel = Label(frame, text='Time (days)')
timeLabel.grid(row=1, column=0)
timeEntry = Entry(frame)
timeEntry.grid(row=1, column=1)
timeVar = tk.IntVar()
timeCheck = tk.Checkbutton(frame, text='Search by Time', variable=timeVar)
timeCheck.grid(row=1, column=2)

authorLabel = Label(frame, text='Author')
authorLabel.grid(row=2, column=0)
authorEntry = Entry(frame)
authorEntry.grid(row=2, column=1)
authorVar = tk.IntVar()
authorCheck = tk.Checkbutton(frame, text='Search by Author', variable=authorVar)
authorCheck.grid(row=2, column=2)

excelLabel = Label(frame, text='Write Excel Workbook?')
excelLabel.grid(row=3, column=1)
excelVar = tk.IntVar()
excelCheck = tk.Checkbutton(frame, text='Excel', variable=excelVar)
excelCheck.grid(row=3, column=2)

##  BUTTONS  ###
searchButton = Button(frame, text ='Search', command = searchAndPrint)
searchButton.grid(row=7  , column = 2)

displayButton = tk.Button(frame, text='Display Video', command=displayPage)
displayButton.grid(row = 8, column=2)


## packing the window   ###
frame.pack()
the_window.mainloop()  #ONLY FOR WINDOWS USERS
