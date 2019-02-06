
def line(): print('-'*25)


class Person(object):

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


	def set_name(self, name):
		if type(name) != str:
			raise TypeError('name must be a str')
		if name==None or name.strip()=='':
			raise ValueError('name cannot be empty')

		self.__name = name

	def get_name(self):
		return self.__name

	# propertes are a pair functions for each member variable
	# that have the same name, one for setter and one for getter.
	# Clients can use them as variables of the object
	# p1.name = 'Vinod' will invoke the setter function
	# print(p1.name) will invoke the getter function

	# getter function
	@property
	def name(self):
		return self.__name

	# setter function for the getter property 'name' defined above
	@name.setter
	def name(self, name):
		if type(name) != str:
			raise TypeError('name must be a str')
		if name==None or name.strip()=='':
			raise ValueError('name cannot be empty')
		self.__name = name
	
	# getter function for property 'city'
	@property
	def city(self):
		return self.__city

	# setter function for the getter property 'city' defined above
	@city.setter
	def city(self, city):
		if city!=None and type(city) != str:
			raise TypeError('city must be a str')
		self.__city = city
	
	# getter function for property 'email'
	@property
	def email(self):
		return self.__email

	# setter function for the getter property 'email' defined above
	@email.setter
	def email(self, email):
		if email!=None and type(email) != str:
			raise TypeError('email must be a str')
		self.__email = email
		
	# getter function for property 'phone'
	@property
	def phone(self):
		return self.__phone

	# setter function for the getter property 'phone' defined above
	@phone.setter
	def phone(self, phone):
		if phone!=None and type(phone) != str:
			raise TypeError('phone must be a str')
		self.__phone = phone
	

def main():
	
	p1 = Person()

	# p1.set_name('Vinod')
	p1.name = 'Vinod'
	p1.city = 'Bengaluru'
	p1.email = 'vinod@vinod.co'
	p1.phone = '9731424784'

	p1.print_info()

if __name__ == '__main__':
	main()









