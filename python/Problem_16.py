# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2**1000?

import math

def sum_of_digits(num):
	"""Find the sum of digits of a number."""
	
	# convert the number to a list of string
	# sum this list.
	return sum([int(x) for x in str(num)])

if __name__ == '__main__':
	print(sum_of_digits(int(math.pow(2,1000))))