
def line(): print('-'*25)


class Person:

	def __init__(self, **kwargs):
		self.__name = kwargs.get('name')
		self.__city = kwargs.get('city', 'Bangalore') 
		self.__email = kwargs.get('email')
		self.__phone = kwargs.get('phone')

	def print_info(self):
		print('Name  =', self.__name)
		print('City  =', self.__city)
		print('Email =', self.__email)
		print('Phone =', self.__phone)
		line()

def main():
	p1 = Person()
	p2 = Person(name='Vinod', country='India')
	p3 = Person(name='Shyam', city='Shimoga')
	p4 = Person(name='John', city='Dallas', email='john@example.com', phone='5559383322')

	p2.__name = 'Ravi'
	p2.__city = 'Chennai'

	p1.print_info()
	p2.print_info()
	p3.print_info()
	p4.print_info()

	print('p2.__name is', p2.__name)
	print('p2.__city is', p2.__city)

	line()

	print(dir(p1))
	line()
	print(dir(p2))

if __name__ == '__main__':
	main()
