from itertools import permutations
k = set()
for w in permutations('аджика'):
	word = ''.join(w)
	if 'аа' not in word: 
		k.add(word)
print(len(k))