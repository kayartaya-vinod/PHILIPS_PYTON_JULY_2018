'''
Using yield to genterate fibonacci numbers
'''

def factorial_generator(limit):

	def factorial(n):
		if n==1: return 1
		return n * factorial(n-1)

	for i in range(1, limit+1):
		yield factorial(i)

def fibo_generator(limit):
	a, b = -1, 1
	count = 0

	while count < limit:
		c = a + b
		yield c

		a = b
		b = c

		count += 1

def main():

	fg = factorial_generator(25)

	for i in fg:
		print(i)


if __name__ == '__main__':
	main()