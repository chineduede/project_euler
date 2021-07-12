"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

from typing import List


def sum_diagonals(n) -> int:
    """Calculate the sum of the diagonals in a spiral"""
    total_sum = 1
    accum = 1
    for i in range(2, n, 2):     #n is the number of sides
        for _ in range(4):
            # Due to the nature of the spiral, the diagonals
            # can be found starting from 1 by adding 2 four 
            # times accumulatively then adding 4 four times 
            # then 6 four times and so on... 
            accum += i
            total_sum += accum
    return total_sum


if __name__ == '__main__':
    print(sum_diagonals(1001))