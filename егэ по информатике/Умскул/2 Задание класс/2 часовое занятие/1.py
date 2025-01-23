# print('x y z w')
# for x in range(2):
# 	for y in range(2):
# 		for z in range(2):
# 			for w in range(2):
# 				if (((not(w <= z)) or (w == y) or x)) == 0:
# 					print(x, y, z, w)
#  w x y z



# def f(x, y, z, w):
# 	return ((not (w <= z)) or (w == y) or x)
# from itertools import *
# for a in product([1, 0], repeat=6):
# 	table = [(1, 0, a[0], 1), (a[1], a[2], 1, 1), (a[3], a[4], 1, a[5])]
# 	if len(set(table)) == 3:
# 		for i in permutations('xyzw'):
# 			if [f(**dict(zip(i, stroka))) for stroka in table] == [0, 0, 0]:
# 				print(i)