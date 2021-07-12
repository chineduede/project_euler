# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def prime_factors(number: int) -> int:
	"""A function to find the largest prime factor of a number.
	
	:number -> Number to find its largest prime factor"""

	i, max_num = 2, 0					#i is the prime factor, max_num is the max prime			
	while i <= number:
		div = number/i					
		if div.is_integer():			#if there is no remainder, i is a factor
			if i > max_num:
				max_num = i
			number = div				#change new number to number / i
		else:
			i += 1
	return max_num

if __name__ == '__main__':
	print(prime_factors(600851475143))

