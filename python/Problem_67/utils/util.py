"""
Read the text triangle.txt and return an array
"""

def read_file(file_loc):
    # opens a file given a file location
    array: list = []
    with open(file_loc) as file:
        for line in file:
            line = line.strip().split()
            array.append([int(i) for i in line])

    return array


if __name__ == '__main__':
    read_file = "../triangle.txt"
    print(main(file_loc))