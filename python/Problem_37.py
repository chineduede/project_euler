# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes

import math

MAX_TRUC_PRIMES = 11

def prime_generator():
    # Implemented with comments in Problem_7.py
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def is_prime(n):
    """Checks if a number is prime"""
    if n == 2: return True
    if n % 2 == 0 or n <= 1: return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0: return False
    return True

def is_truncatable(num: int):
    """Checks if a prime is truncatable by using an inner recursive
    function."""
    def wrapper(x: str, ids=None, ide=None):
        # to avoid unnecessary recursions when the number 
        # is more than 1 digit and is obviously not prime
        if not is_prime(int(x)): return False
        if len(x) <= 1:  return is_prime(int(x))        # base case
        return wrapper(x[ids:ide], ids, ide)
    temp = str(num)
    # Calling the function two different time is easier as a call determines which
    # direction to start truncating.
    return wrapper(temp, 1, None) and wrapper(temp, None, -1)

def trucatable_primes():
    count, trunc_sum = 0, 0
    to_discard = [2, 3, 5, 7]
    for prime in prime_generator():
        if count >= 11: break
        if prime not in to_discard and is_truncatable(prime):
            count += 1
            trunc_sum += prime
            print(f"Found {count}: {prime}, total is now {trunc_sum}")
    print(trunc_sum)


print(trucatable_primes())