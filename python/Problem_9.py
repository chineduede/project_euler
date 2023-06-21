# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math
from typing import Generator, Tuple


def pythagorean_triplets(n: int) -> Generator[Tuple[int, int, int], None, None]:
    """Yields the next pythagorean triplets."""
    for a in range(n):
        for b in range(1, a):
            c = math.sqrt(a * a + b * b)
            if c.is_integer():
                yield a, b, int(c)


def main(n: int):
    for i in pythagorean_triplets(n):
        if sum(i) == 1000:
            return i


if __name__ == '__main__':
    print(math.prod(main(100000)))
