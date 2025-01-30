def f(x, y, z, w):
	return (y and (z <= w) and ((not(z)) <= ((not (w)) == x)))
from itertools import *
for a in product([1, 0], repeat=10):
	table = [(a[0], a[1], 0, 0), (a[2], 0, 0, a[3]), (1, a[4], 1, 1)]
	if len(set(table)) != 3:
		continue
	for i in permutations('xyzw'):
		if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 0]:
			print(i)