print('x y z w')
for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):
				if ((z and (not (x))) or w or (not (y))) == 0:
					print(x, y, w, z)
# from itertools import *
# def f(x, y, w, z):
# 	return (z and (not x)) or w or (not y)
# table = [(0, 1, 0, 0), (0, 1, 1, 0), (1, 1, 1, 0)]
# for i in permutations('xywz'):
# 	if [f(**dict(zip(i, stroka))) for stroka in table] == [0, 0, 0]:
# 		print(i)
# x y z w
# 0 1 0 0
# 1 1 0 0
# 1 1 0 1