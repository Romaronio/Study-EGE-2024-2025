from itertools import permutations
k = set()
for w in permutations('аврора'):
	word = ''.join(w)
	if 'аа' not in word and 'рр' not in word: 
		k.add(word)
print(len(k))