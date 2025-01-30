# from itertools import *
# def f(x,y,z,w):
# 	return (not(w <= z)) or (w == y) or x == 0
# for a in product([0, 1], repeat = 6):
# 	table = [(1, 0, a[0], 1), (a[1], a[2], 1, 1), (a[3], a[4], 1, a[5])]
# 	if len(set(table)) != 3:
# 		continue
# 	for i in permutations('xyzw'):
# 		if [f(**dict(zip(i, stroka))) for stroka in table] == [0,0,0]:
# 			print(i)
