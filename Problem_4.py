# Largest palindrome product
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two
# 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(item):
    """A function to check if an item is a palindrome"""
    if type(item) == int or type(item) == float:
        item = str(item)	
    rev_item = ''.join(list(item)[::-1])
    return rev_item == item

def utility(stop, start, step):
    """function to multiply numbers greater than 100 but less than 1000
    to find the largest palindromic number."""
    max_num = 0
    for i in range(stop, start, step):
        for j in range(stop, start, step):
            number = i * j
            if palindrome(number):
                if number > max_num:
                    max_num = number
    return max_num

  

if __name__ == '__main__':
    print('The largest palindrome is', utility(999, 100, -1))






