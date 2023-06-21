"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1**4 + 6**4 + 3**4 + 4**4
    8208 = 8**4 + 2**4 + 0**4 + 8**4
    9474 = 9**4 + 4**4 + 7**4 + 4**4
    As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

POWERS = {str(num): num**5 for num in range(10)}
START = 2
END = 5 * 9**5  # We do not need to pass this boundary as that is the maximum number that can be created


def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end + 1, 1):
        number = str(i)
        powers = sum([POWERS[x] for x in number])
        if i == powers:
            print(i, [POWERS[x] for x in number])
            total += i
    return total


if __name__ == '__main__':
    print(sum_of_numbers(START, END))
