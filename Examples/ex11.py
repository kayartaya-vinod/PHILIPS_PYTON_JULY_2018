'''
Exception handling
'''


def accept_and_print_total():

	num, total = None, 0
	while num != 0:
		num = input('Enter a number (0 to stop): ')

		try:
			num = int(num)
			total += num
		except ValueError as e:
			# print(e)
			print('You have input a wrong type of value. Please try again')


	print('Total of all inputs is', total)


def basic_math(*args):
	try:
		n = int(args[0])
		d = int(args[1])
		q = n // d # --> integer division in python 3.x
		print('quotent of {} / {} is {}'.format(n, d, q))
	except ValueError:
		print('Invalid value passed as inputs')
		return
	except ZeroDivisionError:
		print('Cannot divide numbers by zero')
	except IndexError:
		print('Not all inputs were supplied')
	except Exception as e:
		print('Something went wrong!', e)
	finally:
		print('Basic math over!')

	print('-'*50)


def main():
	# accept_and_print_total()
	basic_math(123, 22)
	basic_math(123, "22")

	# errorneous calls
	basic_math(123, 'asd') 	# --> ValueError
	basic_math(123, 0)		# --> ZeroDivisionError
	basic_math(123)			# --> IndexError





if __name__ == '__main__':
	main()