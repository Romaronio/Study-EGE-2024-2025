# print('x y z w')
# for x in range(2):
# 	for y in range(2):
# 		for z in range(2):
# 			for w in range(2):
# 				if (y or (not(z)) and (not(z == w)) and ((not(x)))) == 1:
# 					print(x, y, z, w)

# x y z w   ответ: x y z w
# 1 1 0 0 p 
# 1 1 1 0 p
# 1 1 1 1 p


def f(x, y, z, w):
	return (y or (not(z))) and (not(z == w)) and (not(x))
from itertools import *
for a in product([1, 0], repeat=4):
	table = [(1, 1, a[0], a[1]), (a[2], 1, 0, 0), (1, a[3], 1, 0)]
	if len(set(table)) != 3:
		continue
	for i in permutations('xyzw'):
		if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 1]:
			print(i)