from itertools import product
k = 0
for w in product('азимут', repeat=6):
	if w.count('з') + w.count('м') + w.count('т') >= 3:
		k += 1
print(k)