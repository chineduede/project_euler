# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

def factorial(n):
	if n == 1 or n == 0:
		return 1
	else:
		return n * factorial(n-1)

factors = []
for i in range(10):
	factors.append(factorial(i))


def factorion(num):
	fact = 0
	if num == 2 or num == 1:
		return False 
	for j in list(str(num)):
		fact += factors[int(j)]
	if num == fact:
		return True, num
	else:
		return False

def sum_of_factorions(limit):
	empty_list = []
	for number in range(limit):
		f_ = factorion(number)
		if type(f_) == tuple:
			empty_list.append(f_[1])

	return sum(empty_list)

if __name__ == '__main__':
	print(sum_of_factorions(100000))





