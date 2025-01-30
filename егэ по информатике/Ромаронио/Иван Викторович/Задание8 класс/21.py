from itertools import product
k = 0
for i in product('0123456789', repeat=6):
	numd = ''.join(i)
	if numd[0] != '0' and all(int ( numd[i]) % 2 != int ( numd[i + 1]) % 2 for i in range(len(numd) - 1)) and sorted(numd, reverse=True) == list(numd):
		k += 1
print(k)
