'''
Object oriented programming in Python
'''

class Person:

	# shared attribute (by all instances of this class)
	# equivalent of 'static' in C++/Java/C#
	my_list = []

	# constructor is a placeholder for creating/initializing
	# member variables of an object.
	# This method is invoked by python, which passes the reference of
	# the newly constructed object along with other parameters passed by the user
	def __init__(self, name, city):
		# 'self' refers to a unique (single) object that is being constructed
		# we can add new properties to the same
		self.name = name
		self.city = city
	
	# a method which has no arguments is considered as
	# a static method, which only can be called using 
	# a classname
	def print_info(self):
		print('Name  =', self.name)
		print('City  =', self.city)
		print('-'*25)

	# this method is automatically invoked whenever
	# an object of this class is treated as a string.
	# equivalent to toString() of Java and C#
	def __str__(self):
		return '{} lives in {}'.format(self.name, self.city)


def main():

	p1 = Person('Vinod', 'Bangalore') # calls the constructor ( __init()__ )
		
	# invoke the member method using an object (invoking object)
	p1.print_info()

	p2 = Person('John', 'Dallas')
	# p2.my_list.append('vinod')

	p2.print_info()


	print(p1)
	print(p2)

	



if __name__ == '__main__':
	main()


