from itertools import product
k = 0
for i in product('чн', repeat=11):
	w = ''.join(i)
	if w.count('н') == 4 and 'нн' not in w:
		if w[0] == 'ч':
			k += 3 * 4 ** 10
		else: 
			k += 4 ** 11
print(k)
