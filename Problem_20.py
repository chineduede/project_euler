# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!


import math

def sum_of_digits(num):
	num = list(str(num))
	num = [int(x) for x in num]
	return sum(num)

if __name__ == '__main__':
	print(sum_of_digits(math.factorial(100)))