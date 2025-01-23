from itertools import product
k = 0
for w in product('банкир', repeat = 6):
	if w.count('а') < 2 and w.count('и') < 2:
		k += 1
print(k)