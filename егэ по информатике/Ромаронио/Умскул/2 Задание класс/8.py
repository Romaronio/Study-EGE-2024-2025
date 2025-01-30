from itertools import *
def f(x, y, z, w):
	return ((y and (not(x))) or (x == w) or z)
for a in product([1, 0], repeat=4):
	table = [(1, 0, 0, 0), (a[0], a[1], a[2], 1), (1, 1, 0, a[3])]
	if len(set(table)) != 3:
		continue
	for i in permutations('xyzw'):
		if [f(**dict(zip(i, stroka))) for stroka in table] == [0, 0, 0]:
			print(i)