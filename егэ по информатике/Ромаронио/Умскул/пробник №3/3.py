# print('a b c d')
# for a in range(2):
# 	for b in range(2):
# 		for c in range(2):
# 			for d in range(2):
# 				if (not(c <= d) and (d <= a) != (b and c and d and not(a))) == 1:
# 					print(a, b, c, d)
from itertools import *
def f(a, b, c, d):
	return (not(c <= b) and (d <= a) != (b and c and d and not(a)))
for a in product([0, 1], repeat=6):
	table = [(a[0], 0, 0, 0), (a[1], a[2], a[3], 0), (a[4], a[5], 0, 0)]
	if len(set(table)) != 3:
		continue
for i in permutations('abcd'):
	if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 1]:
		print(i)