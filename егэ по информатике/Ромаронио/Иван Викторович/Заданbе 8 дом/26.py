from itertools import product
k = 0
for i in product('чн', repeat=12):
	w = ''.join(i)
	if w.count('н') == 5 and 'нн' not in w:
		if w[0] == 'ч':
			k += 3 * 4 ** 11
		else: 
			k += 4 ** 12
print(k)
