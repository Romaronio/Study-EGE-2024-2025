from itertools import product
k = 0
for w in product('размах', repeat = 6):
	if w.count('р') + w.count('з') + w.count('м') + w.count('х') >= 3:
		k += 1
print(k)