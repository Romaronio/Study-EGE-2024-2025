from itertools import permutations
k = set()
for w in permutations(sorted('варфоломей'), r=6):
	s = ''
	for c in w:
		if c in 'врфлмй': s += 's'
		else: s += 'g'
	if s.count('s') > s.count('g') and not 'gg' in s and w.count('о') <= 1:
		k.add(w)
print(len(k))
