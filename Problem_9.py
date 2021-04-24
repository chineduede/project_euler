import math

def pythagorean_triplets(n):
	for a in range(n):
		for b in range(1, a):
			c = (math.sqrt(a*a + b*b))
			if c.is_integer():
				yield [a, b, int(c)]

def main(n):
	for i in pythagorean_triplets(n):
		if sum(i) == 1000:
			return i
		else:
			continue


if __name__ == '__main__':
	print(math.prod(main(100000)))


	
