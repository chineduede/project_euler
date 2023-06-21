# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?


from python.utils import gen_primes


def main(n: int) -> int:
    """Find the nth prime number"""

    for index, prime in gen_primes():
        if index == n:
            return prime  # return prime if index is equal to n.


if __name__ == '__main__':
    print(main(10_001))
