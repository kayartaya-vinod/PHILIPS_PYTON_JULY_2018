
# function with default list as parameter
def main():
	add_name('vinod')
	add_name('vinay')
	add_name('james')

	names1 = []
	add_name('dokes', names1)
	add_name('robert', names1)
	add_name('miller')
	add_name('ajay')
	all_names = add_name('harish')
	
	print(all_names)
	print(names1)


# parameter assingment with default values is executed only once
# and not when the call is done, but the python comes across
# this definition
def add_name(name, namelist = []):
	namelist.append(name)
	return namelist

if __name__ == '__main__':
	main()

