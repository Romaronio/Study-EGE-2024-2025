# print('x y z')
# for x in range(2):
# 	for y in range(2):
# 		for z in range(2):
# 			if ((y or x) <= (z == y)) == 0:
# 				print(x, y, z)
from itertools import *
def f(x, y, z):
	return ((y or x) <= (z == y))
for a in product([1, 0], repeat=5):
	table = [(0, a[0], 0), (a[1], 0, a[2]), (a[3], a[4], 0)]
	for i in permutations('xyz'):
		if[f(**dict(zip(i, stroka))) for stroka in table] == [0, 0, 0]:
			print(i)