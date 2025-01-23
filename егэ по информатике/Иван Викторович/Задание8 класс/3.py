from itertools import product
k = 0
for w in product('ваяющий', repeat=	4):
	if w[0] != 'й' and any(ch in 'аяюи' for ch in w):
		k += 1
print(k)