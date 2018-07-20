# working with loops

def main():
	# while_loop_example()
	# for_loop_example1()
	# for_loop_example2()
	# for_loop_example3()
	for_loop_example4()

def for_loop_example4():
	num = input('Enter a number: ')
	num = int(num)

	for i in range(1, 11):
		print('{} x {} = {}'.format(num, i, num*i)) 


def for_loop_example3():
	# when looping over a str, you have access to an
	# individual char of the str at a time
	for x in 'johndoe':
		print(x)

def for_loop_example2():
	# when looping over a dictionary using the for loop
	# you have access to the keys
	p1 = {'name': 'Vinod', 'email': 'vinod@vinod.co'}
	for key in p1:
		print(key, ' --> ', p1[key])



def for_loop_example1():
	for name in ('vinod', 'shyam', 'john', 'jane'):
		print('Hello {}'.format(name))

def while_loop_example():
	num = input('Enter a number: ')
	num = int(num)

	i = 1
	while i <= 10:
		print('{} x {} = {}'.format(num, i, num*i)) 
		i += 1


if __name__ == '__main__':
	main()