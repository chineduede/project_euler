# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

def self_powers(n):
    """method for finding self powers and return
    last 10 digits."""
    accum = 0
    for i in range(1, n + 1):
        accum += (i ** i)
    return str(accum)[-10:]


if __name__ == '__main__':
    print(self_powers(1000))
