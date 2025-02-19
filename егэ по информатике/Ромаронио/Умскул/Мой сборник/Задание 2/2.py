# print('xyzw')
# for x in range(2):
#   for y in range(2):
#     for z in range(2):
#       for w in range(2):
#         if ((z <= y) <= x) or not(w) == 0:
#           print(x, y, z, w)


# from itertools import *
# def f(x, y, z, w):
#   return (((z <= y) <= x) or not(w))
#
# for a in product([0, 1], repeat=7):
#   table = [(a[0], 0, a[1], 0), (a[2], 1, 0, a[3]), (a[4], a[5], 1, a[6])]
#   if len(set(table)) != 3:
#     continue
#   for i in permutations('xyzw'):
#     if [f(**dict(zip(i, stroka))) for stroka in table] == [0, 0, 0]:
#       print(i)


# def f(x, y, z, w):
# 	return (y or (not(z))) and (not(z == w)) and (not(x))
# from itertools import *
# for a in product([1, 0], repeat=4):
# 	table = [(1, 1, a[0], a[1]), (a[2], 1, 0, 0), (1, a[3], 1, 0)]
# 	if len(set(table)) != 3:
# 		continue
# 	for i in permutations('xyzw'):
# 		if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 1]:
# 			print(i)





