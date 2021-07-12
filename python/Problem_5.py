# Smallest multiple
# 2520 is the smallest number that can be divided by
# each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?


def find_lcm_small(array):
    """find the lcm of an array of numbers"""
    list_x = array[:]
    while len(set(list_x)) != 1:    #when equals one, all numbers are the same, we have the lcm
        min_value = min(list_x)     #find the min value of the array
        min_value_index = list_x.index(min_value)
        list_x[min_value_index] = min_value + array[min_value_index]    #add the min_value to itself
    return list_x[0]           


def find_lcm_big(array):
    """Find the lcm of a longer array by breaking it into fours"""
    empty_list = []
    new_list = [array[i:i+4] for i in range(0,len(array),4)]
    for sub_list in new_list:
    	empty_list.append(find_lcm_small(sub_list))
    return find_lcm_small(empty_list)


if __name__ == '__main__':
    print(find_lcm_big([i for i in range(1, 21)]))