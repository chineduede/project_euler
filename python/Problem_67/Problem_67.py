"""
Maximum path sum II

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.
          3
         7 4
        2 4 6
       8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE_: This is a much more difficult version of Problem 18. 
It is not possible to try every route to solve this problem, as there are 299 altogether! 
If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all.
There is an efficient algorithm to solve it. ;o)"""

from typing import Generic, List, TypeVar
from utils.util import read_file


T = TypeVar("T", int, list)

class Stack(Generic[T]):
    """A minimal implementation of a stack"""

    def __init__(self) -> None:
        self._container: List[int] = []

    @property
    def is_empty(self) -> bool:
        return not self._container

    @property
    def length(self) -> int:
        return len(self._container)

    def pop(self) -> T:
        return self._container.pop()

    def push(self, item: T) -> None:
        self._container.append(item)

    def stackify(self, array: List) -> None:
        """Takes an array and adds its elements to the stack"""
        for ele in array:
            self._container.append(ele)

    def __repr__(self):
        return repr(self._container)



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
        # array. Elements initiallized to None for easier 
        # insertion while in the loop
        length = min(len(arr1), len(arr2))      #minimum length of both arrays
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
    array: list = read_file("./triangle.txt")
    print(maximum_path(array))
