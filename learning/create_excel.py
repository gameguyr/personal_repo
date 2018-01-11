#! /Users/rlego/anaconda/bin/python

#####################
# PURPOSE: to learn how to write an excel file
#
# DATE: Wed Oct 22 16:10:06 PDT 2014
#
# AUTHOR: Russell Lego
####################

import xlsxwriter


keys = ['campaign_placement_id','total_cost']
ids = [1, 2, 3, 4, 5, 6, 7]
costs = [34, 24,56, 67 , 87, 34, 54]
list_of_values = [ids, costs]

my_dict = {}
for i in range(0, len(keys)):
	my_dict[keys[i]]=list_of_values[i]


#creating the specs for the file

name_of_file = '/Users/russell.lego/Dropbox/PythonWorkspace/learning/test_excel_file.xlsx'
workbook = xlsxwriter.Workbook(name_of_file)
worksheet = workbook.add_worksheet()




# actually writing the data

row = 1
col = 0
for i in range(0, len(keys)):
	worksheet.write(row, col, my_dict.keys()[i])
