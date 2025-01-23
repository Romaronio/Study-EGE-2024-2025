from itertools import product
k = 0
for w in product('012345678', repeat=6):
		if w[0] not in '01357' and w[-1] not in '23' and w.count('1') >= 2:
			k += 1
print(k)