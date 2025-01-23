from itertools import *
def f(x, y, z, w):
	return (not(x)) and ((z <= y) <= w)


for a in product([0,1], repeat=4):
	table = [(0, a[0], 1, a[1]), (1, a[2], 0, 1), (0, 0, a[3], 1)]
	if len(set(table)) != 3:
		continue
	for i in permutations('xyzw'):
		if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 0]:
			print(i)