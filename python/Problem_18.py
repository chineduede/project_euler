"""
Maximum path sum I

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.
          3
         7 4
        2 4 6
       8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:"""

from typing import List
from python.utils import Stack

triangle = [
    [75],
    [95, 64],
    [17, 47, 82, ],
    [18, 35, 87, 10, ],
    [20, 4, 82, 47, 65, ],
    [19, 1, 23, 75, 3, 34, ],
    [88, 2, 77, 73, 7, 63, 67, ],
    [99, 65, 4, 28, 6, 16, 70, 92, ],
    [41, 41, 26, 56, 83, 40, 80, 70, 33, ],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29, ],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, ],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, ],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, ],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, ],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23, ],
]


def maximum_path(triangle: List[int]) -> int:
    stack: Stack[List[int]] = Stack()
    stack.stackify(triangle)

    while stack.length > 1:
        # the array at the top of the stack which is
        # the base of the triangle
        arr1: List[int] = stack.pop()
        # the next element/array
        arr2: List[int] = stack.pop()
        # initialize an empty array with length of the shorter
        # array. Elements initialized to None for easier
        # insertion while in the loop
        length = min(len(arr1), len(arr2))  # minimum length of both arrays
        temp: List[int] = [None] * length
        for i in range(length):
            # Movement in a triangle can only happen between the ith element
            # and the ith bottom adjacent element and the i + 1 element
            temp[i] = max(arr2[i] + arr1[i], arr2[i] + arr1[i + 1])
        # push the additions to the top of the stack
        stack.push(temp)

    # only one array/element of the stack left
    # with only one element which signifies the
    # maximum path from a bottom-up approach
    return stack.pop()[0]


if __name__ == '__main__':
    t = [
        [3, ],
        [7, 4, ],
        [2, 4, 6],
        [8, 5, 9, 3],
    ]
    print(maximum_path(triangle))
