# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


def gen_primes(): 
    """Generate infinite sum of primes using seive of eratosthenes"""
    D = {}
    q, count = 2, 1
    while True:
        if q not in D:
            yield q, count
            count += 1
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def sum_of_prime(n):
	"""A function to calculate the sum of primes within a given range n"""
	summation = 0
	for i in gen_primes():
		prime, _ = i
		if prime > n:
			break
		summation += prime

	return summation

if __name__ == '__main__':
	print(sum_of_prime(2000000))
