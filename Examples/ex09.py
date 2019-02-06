'''
	working with files
'''

def read_file_ex_1(filename):
	file = open(filename, 'rt')
	content = file.read() # reads the entire content and returns
	file.close()

	print(content)

def read_file_ex_2(filename):
	file = open(filename, 'rt')
	lines = file.readlines() 
	file.close()

	for line in lines:
		print(line, end='')
	
def read_file_ex_3(filename):
	file = open(filename, 'rt')

	for line in file:
		print(line.rstrip())

	file.close()


def read_file_ex_4(filename):
	with open(filename) as file:
		for line in file:
			print(line.rstrip())


def main():
	filename = input('Enter a filename: ')
	read_file_ex_4(filename)

if __name__ == '__main__':
	main()




