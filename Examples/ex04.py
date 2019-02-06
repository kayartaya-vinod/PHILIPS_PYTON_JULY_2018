'''
Testing ex03 functions
'''

print('The name of this module (ex04) is ', __name__)

import ex03

year = int(input('Enter a year: '))
print('{} is a leap year ? {}'.format(year, ex03.is_leap(year)))