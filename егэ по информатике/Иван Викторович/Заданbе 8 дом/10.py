from itertools import permutations
k = set()
for w in permutations('аттестат'):
	s = ''
	for i in w:
		s += 'g' if i in 'ae' else 's'
		if 'ss' in s or 'gg' in s:
			k.add(w)
print(len(k))