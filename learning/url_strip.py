

import re
import pdb

file_1_path = '/Users/russell.lego/Downloads/url_liverail.txt'
file_2_path = '/Users/russell.lego/Downloads/url_liverail_stripped.txt'


file_1 = open(file_1_path, 'r')
file_2 = open(file_2_path, 'w')

lines = file_1.readlines()

for i in range(1, len(lines)):
	match_check = 0
	match = re.findall('\w{1}/\w{1}', lines[i])

	if len(match)!= 0:
		index = lines[i].index(re.findall('\w{1}/\w{1}', lines[i])[0][1:])
		file_2.write(lines[i][:index]+'\n')
	else:
		file_2.write(lines[i]+'\n')

