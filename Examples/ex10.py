'''
A utility python script for
1. converting a json file into a csv file
2. converting a csv file into a json file
'''

import json

def strip_quotes(arr):
	return [x[1:-1].rstrip() for x in arr]


def csv2json(csv_filename = None, json_filename = None):
	if csv_filename==None:
		csv_filename = input('Enter CSV file to open: ')
	if json_filename==None:
		json_filename = input('Enter JSON file to create: ')

	with open(csv_filename) as csv_file:
		col_names = csv_file.readline().split(',')
		data = csv_file.readlines()
		dict_data = [ dict(zip(strip_quotes(col_names), strip_quotes(d.split(','))))  for d in data]

		with open(json_filename, mode='wt') as json_file:
			json.dump(dict_data, json_file, indent=4)


def json2csv(json_filename = None, csv_filename = None):

	if json_filename==None:
		json_filename = input('Enter JSON filename: ')

	if csv_filename==None:
		csv_filename = input('Enter CSV filename: ')

	with open(json_filename) as json_file:
		data = json.load(json_file)
		# data is a list of dicts
		# need to convert into a list of strings, where 
		# each string is the comma separated values for each dict
		csv_data = [ dict2csv(d) for d in data]
		with open(csv_filename, mode='wt') as csv_file:
			headers = ','.join(['\"'+str(x)+'\"' for x in data[0].keys()]) + '\n'
			csv_file.write(headers)
			
			csv_file.writelines(csv_data)
	
def dict2csv(data):
	return ','.join(['\"'+str(x)+'\"' for x in data.values()]) + '\n'


def main():
	# json2csv('contacts.json')
	csv2json('contacts_v2.csv', 'contacts_v2.json')

if __name__ == '__main__':
	main()
