from itertools import permutations
k = set()
for w in permutations('веретено'):
	s = ''
	for i in w:
		s += 'g' if i in 'ео' else 's'
	if 'gg' not in s and 'ss' not in s:
		k.add(w)
print(len(k))