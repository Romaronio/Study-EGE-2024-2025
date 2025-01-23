from itertools import permutations
k = set()
for w in permutations('добрыня', r=6):
	s = ' '
	for c in w:
		if c in 'дбрн': s += 's'
		else: s += 'g'
	if s.count('s') > s.count('g') and not 'gg' in s:
		k.add(w)
print(len(k))
