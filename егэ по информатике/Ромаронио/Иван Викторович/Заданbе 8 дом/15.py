from itertools import product
for i, w in enumerate(product(sorted('сено'), repeat=4), 1):
	if w[0] == 'с':
		print(i)
		break