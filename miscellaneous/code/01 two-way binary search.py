import math, random

# only <= is allowed and counted (#op = 1)
# a == b <=> a <= b and b <= a (#op = 2)
# a  < b <=> not b <= a (#op = 1)

def log(n):
	if n == 0 : return 0
	return math.log(n)

def binarysearch(k, v, i, j):
	if i == j: return 0, i, 0

	p = (i + j) // 2

	if k == v[p] : return 1, p, 2

	elif k < v[p] : f, w, o = binarysearch(k, v, i, p)

	else : f, w, o = binarysearch(k, v, p + 1, j)

	return f, w, o + 3


def twbinarysearch(k, a, b, v, i, j):
	if a == b or i == j: return 0

	p = (i + j) // 2

	f, w, o = binarysearch(v[p], k, a, b)

	if f == 1 : k[w] = True

	o += twbinarysearch(k, a, w, v, i, p)
	o += twbinarysearch(k, w + f, b, v, p + 1, j)

	return o




def main(n):

	v = list(range(n))

	for i in range(n):
		f, w, o = binarysearch(i, v, 0, n)
		print(f, w, o / log(n))

	for i in range(1, n//10):
		k = list(range(i))
		o = twbinarysearch(k, 0, i, v, 0, n)
		print(k, o, o / (i * (log(n) - log(i))))



if __name__ == '__main__':
	import sys
	main(int(sys.argv[1]))
