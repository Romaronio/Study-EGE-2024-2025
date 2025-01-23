from itertools import permutations
k = set()
for w in permutations('авторота'):
	s = ''
	for i in w:
		s += 'g' if i in 'ао' else 's'
	if 'ss' not in s and 'gg' not in s:
		k.add(w)
print(len(k))