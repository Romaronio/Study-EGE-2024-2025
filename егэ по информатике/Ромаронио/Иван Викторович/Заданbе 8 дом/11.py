from itertools import product
k = []
for i in product('аоу', repeat=5):
	k += i
print(k[209])