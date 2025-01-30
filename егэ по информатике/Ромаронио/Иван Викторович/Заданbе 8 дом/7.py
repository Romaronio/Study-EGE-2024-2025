from itertools import permutations
k = set()
for w in permutations('шанель'):
	word = ''.join(w)
	if word[0] != 'ь' and 'еаь' not in word:
		k.add(word)
print(len(k))