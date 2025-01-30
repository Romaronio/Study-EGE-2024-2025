from itertools import permutations
m = set()
for s in permutations('кайф'):
	if 'кф' not in s and s[0] != 'й':
		m.add(s)
print(len(m), m)