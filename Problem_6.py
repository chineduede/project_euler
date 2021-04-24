# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + ... + 10**2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)**2 = 55**2 = 3025$$

# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640$.

# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

def sum_of_squares(n):
	"""A function for finding sum of squares in a given range n"""
	count = 0
	for i in range(1, n):
		count += (i ** 2)
	return count

def square_of_sum (n):
	"""A function for finding square of sums in a given range n."""
	sum = 0
	for i in range(1, n):
		sum += i
	return sum ** 2

def difference(n):
	"""A function for finding difference between a range's squares and sum"""
	return square_of_sum(n) - sum_of_squares(n)



if __name__ == '__main__':
	print(difference(101))