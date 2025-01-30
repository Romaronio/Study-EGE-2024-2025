from itertools import permutations
k = []
for w in permutations('малина'):
	word = ''.join(w)
	if 'аа' not in word:
		k.append(word)
print(len(k))