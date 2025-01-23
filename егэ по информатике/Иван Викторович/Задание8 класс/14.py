from itertools import product
for i, x in enumerate(product(sorted('алгоритм'), repeat=4), 1):
	word = ''.join(x)
	if word[:2] == 'го':
		print(i)
		break