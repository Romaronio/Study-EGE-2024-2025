# from itertools import *
# def f(x, y, z, w):
# 	return (((z <= x) or ((not(w)) and y)) == (y == x))
# for a in product([1,0], repeat=4):
# 	table = [(a[0], 1, 0, 0), (0, 1, a[1], a[2]), (0, 0, 0, 1)]
# 	for i in permutations('xyzw'):
# 		if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 1]:
# 			print(i)

# for x in range(2):
# 	for y in range(2):
# 		for z in range(2):
# 			for w in range(2):
# 				if (((z <= x) or ((not(w)) and y))== (y == x)) == 1:
# 					print(x, y, z, w)
