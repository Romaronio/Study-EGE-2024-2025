from itertools import permutations
k = set()
for w in permutations('айсберг'):
	word = ''.join(w)
	if word[0] != 'й' and 'йа' not in word and 'йе' not in word:
		k.add(word)
print(len(k))