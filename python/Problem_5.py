# Smallest multiple
# 2520 is the smallest number that can be divided by
# each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible 
# by all the numbers from 1 to 20?

import math


def lcm_of_array(array: list) -> int:
    """A function to calculate the lowest common multiple of
    an array of integers."""

    # get the first number which is 
    # the lcm of itself.
    lcm = array[0]
    for num in array:
        # start from the first number and
        # find the gcd of the number and the
        # present lcm, use floor division to
        # get integer result.
        lcm = lcm * (num // math.gcd(lcm, num))
    return lcm


if __name__ == '__main__':
    arr = [i for i in range(1, 21)]
    print(lcm_of_array(arr))
