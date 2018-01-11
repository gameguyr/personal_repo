#!/usr/bin/python

from ODSReader import *

doc = ODSReader("~/Documents/Python_Projects/MyTest.ods")
table = doc.getSheet("Sheet1")
firstRow = table[0]
print firstRow
firstCellOfFirstRow = firstRow[0]
print firstCellOfFirstRow

print "type of first row is: ",type(firstRow)
print "type of first cell is: ",type(firstCellOfFirstRow)  
