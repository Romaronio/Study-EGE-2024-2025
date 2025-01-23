def f1(x, y, z, w):
	return ((x == y) and (w <= z))
def f2(x, y, z, w):
	return ((x <= y) <= (z == w))
from itertools import *
for a in product([1, 0], repeat=4):
	table = [(1, a[0], 1, 1), (0, 1, 0, a[1]), (a[2], 0, 0, a[3])]
	if len(set(table)) != 3:
		continue
	for i in permutations('xyzw'):
		if [f1(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 0]:
			for m in product([1, 0]):
				if [f2(**dict(zip(i, stroka))) for stroka in table] == [0, m[0], 0]:
					print(i)