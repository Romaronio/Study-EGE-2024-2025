from itertools import *
k = 0
for i in permutations('кайф', r=4):
	word = ''.join(i)
	if word[-1] != 'й':
		if 'кф' not in word:
			k += 1
print(k)
