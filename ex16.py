from ex15 import Person
from ex18 import *

class Employee(Person):
	
	# overriding the super/base class constructor
	def __init__(self, **kwargs):
		# unlike in Java/C++/C#, this is a regular function call
		# and can be done anywhere inside this function and
		# any number of times
		Person.__init__(self, **kwargs)
		# super().__init__(**kwargs)

		self.__id = kwargs.get('id')
		self.__dept = kwargs.get('dept', 'POOL')

		# invokes the 'salary' setter function
		self.salary = kwargs.get('salary', 25000)

	# overriding the print_info() from the base/super class
	def print_info(self):
		print('Id    =', self.__id)
		print('Dept  =', self.__dept)
		print('Salry =', self.__salary)
		# Person.print_info(self)
		super().print_info()

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, id):
		self.__id = id


	@property
	def dept(self):
		return self.__dept

	@dept.setter
	def dept(self, dept):
		self.__dept = dept


	@property
	def salary(self):
		return self.__salary

	@salary.setter
	def salary(self, salary):
		if salary < 25000:
			raise SalaryException('Salary must be >= Rs.25000')
		self.__salary = salary

	# operator overloded methods
	def __iadd__(self, value):
		if value==None: return self

		if type(value) == str:
			self.name += value
		elif type(value) in (int, float) and value>0:
			self.salary += value
		return self

	def __lt__(self, value):
		if type(value) in (int, float):
			return self.salary < value
		else:
			raise TypeError('Invalid type for value {}'.format(value))

def main():
	e1 = Employee(id=7788, name='scott', email='scott@mycomp.com', 
		dept='PRODUCTION', salary=55000)

	e1.print_info()
	
	e1 += ' ross'					# e1.__iadd__('ross')
	if e1 < 50000: e1 += 5000		# e1.__iadd__(5000)

	e1.print_info()

	# testing SalaryException
	e2 = Employee(id=890, name='James', salary=5000)
	e2.print_info()


	# print(dir(e1))

if __name__ == '__main__':
	main()