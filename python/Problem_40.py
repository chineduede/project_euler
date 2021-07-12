# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000


def champernownes_const():
	"""A generator that yields the next digit of the champernownes constant"""
	string, index = '', 0
	while True:
		for i in string:					#yield the first character
			yield i
		index += 1
		string = str(index)					#concatenate number to string


def main(limit):
	accum, count = 1, 0
	for i in champernownes_const():
		if count == limit:
			return accum
		count += 1
		if count == 1 or count == 10 or count == 100 or \
			count == 1000 or count == 10000 or count == 100000 \
			or count == 1000000:
			accum *= int(i)



if __name__ == '__main__':
	print(main(1000001))





