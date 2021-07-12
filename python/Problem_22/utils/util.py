"""
Read the names.txt file and returns a list of sorted names
"""

from typing import Dict, List
from string import ascii_uppercase


def parse_names(file_loc) -> List[str]:
    """Read the file from file loc and returns it."""
    array: List[str] = []
    with open(file_loc) as file:
        for line in file:
            line = line.strip().split(",")
            array.extend([name[1:-1] for name in line])
    array.sort()
    return array


MAPPING: Dict[str, int] = {}
for index, letter in enumerate(ascii_uppercase, 1):
    MAPPING[letter] = index


if __name__ == '__main__':
    print(parse_names("../names.txt"))
    # print(ascii_uppercase)
    print(MAPPING)

