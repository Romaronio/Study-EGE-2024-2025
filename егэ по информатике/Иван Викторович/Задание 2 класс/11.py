from itertools import *

def f(x, y, z, w):
	return (not z) and x and (y <= w)

for s in product([0, 1], repeat=5):
	table = [(1, s[0], s[1], 0), (s[2], s[3], 1, 1), (1, 0, 1, s[4])]
	if len(table) == len(set(table)):
		for n in permutations('xyzw'):
			if [f(**dict(zip(n, line))) for line in table] == [1, 1, 0]:
				print(n)
