from itertools import permutations
k = 0
for i in permutations('чн', r=12):
	w = ''.join(i)
	if w[-1] in '05' and w[0] != '0' and all(int(w[i]) % 2 != int(w[i + 1]) % 2 for i in range(len(w) - 1)):
		k += 1
print(k)
