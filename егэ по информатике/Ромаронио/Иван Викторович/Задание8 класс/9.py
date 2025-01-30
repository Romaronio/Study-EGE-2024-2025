from itertools import permutations
k = set()
for w in permutations('аммиакат'):
	s = ''
	for i in w:
		s += 'g' if i in 'аи' else 's'
	if 'ss' in s or 'gg' in s:
		k.add(w)
print(len(k))