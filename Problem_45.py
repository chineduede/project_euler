import math

class FigurateNumbers():
	"""A not so neccessary class for finding figurate numbers.
	Using plain functions would be less verbose. """

	def __init__(self, limit):
		self._limit = limit
		self._count = 0
		self._list_equality = []			#list of numbers both hexagonal, pentagonal and triangular

	def _hexagonalNumber(self):
		n = 2
		while True:
			yield (n * (2 * n - 1))
			n += 1

	def checkEquality(self):
		for number in self._hexagonalNumber():
			if self._count <= self._limit:
				index =  (math.sqrt(24 * number + 1) + 1)/6
				self._count += 1
				if index.is_integer():
					self._list_equality.append(int((index * (3 * index - 1))/ 2))
			else:
				break
		return self._list_equality

if __name__ == '__main__':
	new = FigurateNumbers(1000000)
	print(new.checkEquality())
	old = FigurateNumbers(10000)
	print(old.checkEquality())


