"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 

        COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
        So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

from typing import List
from utils.util import MAPPING, parse_names

names = parse_names("./names.txt")

def name_sum(name) -> int:
    """Finds the sum of individual letters in a name using
    a dictionary ({a: 1, b: 2, ...}) MAPPING as lookup."""
    accum: int = 0          #accumulator
    for letter in name:
        accum += MAPPING[letter]
    return accum

def total_names_sum(names: List[str]) -> int:
    """Returns the total of all the names scores in the names array."""
    accum: int = 0
    for index, name in enumerate(names, 1):
        name_score = index * name_sum(name)
        accum += name_score
    return accum

if __name__ == '__main__':
    print(total_names_sum(names))