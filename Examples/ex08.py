'''
Working with function arguments

1. mandatory (positional/keyword) arguments
2. arguments with default values (optional arguments)
3. arbitrary arguments (variable length arguments)
4. keyword arguments (dictionary arguments)
'''

def print_info_1(name, email, city='bangalore'):
	print('Name  =', name)
	print('Email =', email)
	print('City  =', city)
	print('--'*25)

# arbitrary (variable length) arguments
# only one tuple is allowed as a formal argument
def print_total(*args):
	print('type of args is', type(args))
	print('args contain', args)
	total = sum([v for v in args if type(v) in (int, float)])
	print('Total is', total)
	print('--'*25)

def print_info(name, email, *phones):
	print('Name    =', name)
	print('Email   =', email)
	print('Phones  =', phones)
	print('--'*25)

def print_student_info(**kwargs):

	print('type of kwargs is', type(kwargs))

	# check for mandatory fields 
	# and raise error if they dont exist

	if('name' not in kwargs): raise KeyError('name is missing')
	if('subjects' not in kwargs): raise KeyError('subjects is missing')

	for key in kwargs:
		print(key, '-->', kwargs[key])
	print('--'*25)

def main():
	print_student_info(name='Vinod', 
		phones = ['9731424784', '9844083934'],
		subjects = ['physics', 'maths', 'electronics'],
		email = {'vinod@vinod.co', 'vinod@example.com'},
		address = dict(city='bangalore', state='ka'))


	print_info('vinod', 'vinod@vinod.co', '9731424784', '984408393')

	print_total(10, 29, 30, 5, 'vinod', 383, 222)

	# print_info_1() # error; must supply 2 arguments
	print_info_1('vinod', 'vinod@vinod.co')

	data = ['kumar', 'kumar@example.com', 'mysore'] # could be set or tuple 
	# set does not guarantee the order of insersion
	print_info_1(*data)

	data = dict(email='john@example.com', name='john', city='dallas')
	print_info_1(**data)



if __name__ == '__main__':
	main()