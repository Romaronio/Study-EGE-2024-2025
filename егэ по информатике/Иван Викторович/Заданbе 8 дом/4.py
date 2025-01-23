from itertools import product
k = 0
s = ''
for w in product('енисей', repeat=4):
		if  w[0] != 'й' and w.count('е') + w.count('и') >= 1:
			k += 1
print(k)