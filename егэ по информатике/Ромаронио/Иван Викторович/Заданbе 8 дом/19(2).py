from itertools import product
k = 0 
for w in product('01234567', repeat=5):
	if w[0] in '2468' and w[-1] not in '26' and w.count('7') <= 2:
		k += 1
print(k)