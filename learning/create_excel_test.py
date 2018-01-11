#! /Users/rlego/anaconda/bin/python

#####################
# PURPOSE: to learn how to write an excel file
#
# DATE: Wed Oct 22 16:10:06 PDT 2014
#
# AUTHOR: Russell Lego
####################

import xlsxwriter
import pickle
import os
import pdb



#function to write the data to the worksheet
def write_data_to_worksheet(ouput_filename, column_names, query_results_matrix ):
	workbook = xlsxwriter.Workbook(ouput_filename)
	worksheet = workbook.add_worksheet()

	# writing the column names to the file
	row = 0
	col = 0 
	for i in range(0, len(column_names)):
		worksheet.write(row, col, column_names[i])
		col+=1
	# pdb.set_trace()
	# writing the data to the worksheet	
	row = 2
	col = 0 
	for j in range(0, len(query_results_matrix)):
		row = 1+int(j)
		col = 0
		for i in range(0, len(query_results_matrix[j])):
			worksheet.write(row, col, query_results_matrix[j][i])
			col+=1


	workbook.close()


#running the main part
if __name__ == '__main__':
	#getting all columns names and results form the test query, will have to change for full autmation in final product
	column_names = ['campaign_placement_id','total_cost', 'daily_budget', 'imps', 'wins', 'cost_to_budget_ratio']
	results = pickle.load(open('/Users/russell.lego/Dropbox/PythonWorkspace/tubemogul/app-eng/projects/campaign_placement_overspend/campaign_placement_overspend_test.dat', 'r'))
	name_of_file = '/Users/russell.lego/Dropbox/PythonWorkspace/learning/test_excel_file.xlsx'
	write_data_to_worksheet(name_of_file, column_names, results)
	os.system('open %s' % (name_of_file))





