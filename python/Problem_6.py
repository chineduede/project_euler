# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + ... + 10**2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)**2 = 55**2 = 3025$$

# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640$.

# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.


def difference(n: int) -> int:
	"""A function for finding difference between a range's squares and its sum.
	
	:n -> Limit for range, lower boundary is 0"""

	# sum_of_squares is a accumulation of each 
	# number within a range. square_of_sum is 
	# squaring the accumulation of the numbers
	# in a range.
	sum_of_squares, square_of_sum = 0, 0
	for num in range(1, n + 1):
		sum_of_squares += num ** 2					# square each number and accumulate
		square_of_sum += num		
	return (square_of_sum ** 2) - sum_of_squares	# return the difference


if __name__ == '__main__':
	print(difference(100))
