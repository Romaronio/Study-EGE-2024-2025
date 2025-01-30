from itertools import *
k = 0
for w in permutations('чн', repeat=4):
	if w.count('9') == 1 and w[0] != '0' and len([i for i in w if i in 'bcd']) < 4:
		k += 1
print(k)