'''
User defined functions

Author: Vinod
Email : vinod@vinod.co

Following functions exist:
1. is_leap

'''

def main():
	print('2000 is leap ? ', is_leap(2000))
	print('1996 is leap ? ', is_leap(1996))
	print('1997 is leap ? ', is_leap(1997))
	print('1900 is leap ? ', is_leap(1900))
	print('2100 is leap ? ', is_leap(2100))

# definition
def is_leap(year):
	'''
	This function should accept an year
	and return true or false
	based on the year

	Year divisible by 4 and not by 100 is a leap year
	or
	Year divisible by 400 is a leap year
	'''

	if year%400==0 or (year%4==0 and year%100!=0):
		return True
	else:
		return False


# call only if this module is run directly (and not by import)
if __name__ == '__main__':
	main()








