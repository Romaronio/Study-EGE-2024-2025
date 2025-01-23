from itertools import product
k = 0
for i in product('012345678', repeat=7):
	if i[0] not in '260' and i[-1] != i[-2]:
		k += 1
print(k)
