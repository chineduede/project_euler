# Starting in the top left corner of a 2×2 grid,
# and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?


def lattice_paths(row: int, col: int=None) -> int:
	"""A function to count the number of lattice paths
	given num of rows (row), and num of columns (col).
	If col is not given, assumed to be a square lattice."""

	col = row if col is None else col 
	lattice = [1] * (col + 1)			#initializes an array of ones
	for _ in range(row):
		for i in range(col):
			lattice[i+1] += lattice[i]
	return lattice[-1]


if __name__ == '__main__':
	print(lattice_paths(20))