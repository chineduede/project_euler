# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples(limit: int) -> int:
    """A function to find the sum of multiples
    of 3 and 5.

    :limit -> The upper boundary."""
    accum = 0
    for num in range(1, limit):  # loop to limit
        if (num % 3 == 0) or (num % 5 == 0):
            accum += num  # number is a multiple, add to accumulator
    return accum


if __name__ == '__main__':
    print(multiples(1000))
