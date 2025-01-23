from itertools import *
k = 0
for n in product('012345678', repeat=7):
	w = ''.join(n)
	if w[0] != '0' and w[-1] not in '347':
		if any(w[i] == w[i + 1] == w[i + 2] for i in range(len(w) - 2)):
			continue
		else:
			k += 1
print(k)
