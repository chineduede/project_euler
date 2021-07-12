# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2**1000?

import math

def sum_of_digits(num):
	num = list(str(num))
	num = [int(x) for x in num]
	return sum(num)
if __name__ == '__main__':
	print(sum_of_digits(int(math.pow(2,1000))))