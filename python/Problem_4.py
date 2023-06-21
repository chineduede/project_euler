# Largest palindrome product
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two
# 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

from typing import Any


def palindrome(item: Any) -> bool:
    """A function to check if an item is a palindrome."""
    # convert to string if item is number
    # reverse and compare with self
    return ''.join(reversed(str(item))) == str(item)


def utility(start: int, stop: int, step: int) -> int:
    """A Function to multiply numbers greater than start but less than stop
    increasing step at a time in order to find the largest palindromic number
    within the range.
    
    start -> Lower boundary
    stop -> Upper boundary
    step -> incrementor
    """
    max_num = 0  # max palindromic number found
    for i in range(stop, start, step):
        for j in range(stop, start, step):
            number = i * j  # multiply two numbers together
            if palindrome(number) and number > max_num:
                max_num = number  # number is the largest palindrome
    return max_num


if __name__ == '__main__':
    print('The largest palindrome is', utility(100, 999, -1))
