"""
Read the text triangle.txt and return an array
"""

from typing import Generator, Tuple

__all__ = ["read_file", "gen_primes", "sum_of_digits"]


def read_file(file_loc: str) -> list[list[int]]:
    # opens a file given a file location
    array: list[list[int]] = []
    with open(file_loc) as file:
        for line in file:
            line = line.strip().split()
            array.append([int(i) for i in line])

    return array


def gen_primes() -> Generator[Tuple[int, int], None, None]:  # sieve of erasthothenes
    """ Generate an infinite sequence of prime numbers.
    using sieve of erasthothenes.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    prime_dict = {}

    # The running integer that's checked for primeness
    q = 2
    index = 1
    while True:
        if q not in prime_dict:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            yield index, q
            index += 1
            prime_dict[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            for p in prime_dict[q]:
                prime_dict.setdefault(p + q, []).append(p)
            del prime_dict[q]

        q += 1


def sum_of_digits(num):
    """Find the sum of digits of a number."""

    # convert the number to a list of string
    # sum this list.
    return sum([int(x) for x in str(num)])
