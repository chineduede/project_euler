# The following iterative sequence is defined for the set of positive integers:

	# n → n/2 (n is even)
	# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
	# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem),it is thought 
# that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

def collatz_sequence(n: int) -> int:  
	"""Given a number, find the count of the numbers present
	in the collatz sequence.
	"""
	count = 1
	while n != 1:
		count +=1
		# if number is even divide by 2
		# else multiply by 3 and add 1
		n = n/2 if n % 2 == 0 else 3 * n + 1
	return count								# return the count of numbers


def main(limit: int) -> int:
	"""Find the number with the longest collatz sequence
	under limit.
	
	:limit -> Upper boundary."""

	# store collatz sequence count
	table = {}					
	# check only odd numbers as 
	# even numbers wouldn't be long enough
	for i in range(1, limit, 2):				
		table[i] = collatz_sequence(i)
	return max(table, key=table.get)			# return the maximum sequence

if __name__ == '__main__':
	print(main(1000000))
