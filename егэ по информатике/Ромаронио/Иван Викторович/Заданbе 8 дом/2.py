from itertools import product
k = 0
for w in product('ПРОЛо', repeat=5):
	if w.count('а') < 2 and w.count('у') < 2:
		k += 1
print(k)