from itertools import *
def f(x, y, z, w):
	return (w or (not(z))) and x and (not(y))
table = [[0,0,0,1], [0,1,1,1], [0,1,0,1]]
for i in permutations('xywz'):
	if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 1]:
			print(i)
