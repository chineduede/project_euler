# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?


from typing import Generator, Tuple


def gen_primes() -> Generator[Tuple[int, int], None, None]:         #sieve of erasthothenes*
    """ Generate an infinite sequence of prime numbers.
    using sieve of erasthothenes.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    index = 1
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            yield index, q
            index += 1
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

def main(n: int) -> int:
    """Find the nth prime number"""

    for index, prime in gen_primes():
    	if index == n:
    		return prime                # return prime if index is equal to n.

if __name__ == '__main__':
    print(main(50))