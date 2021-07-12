# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# seive of erasthothenes implementation already
# in Problem_7
from problem_7 import gen_primes

def sum_of_prime(n: int) -> int:
	"""A function to calculate the sum of primes within a given range n"""
	summation = 0
	for _, prime in gen_primes():
		if prime > n:
			return summation        #return the total summation if limit reached
		summation += prime


if __name__ == '__main__':
	print(sum_of_prime(2000000))
