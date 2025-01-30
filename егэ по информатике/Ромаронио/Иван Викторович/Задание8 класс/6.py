from itertools import permutations
k = set()
for w in permutations('надпись'):
	word = ''.join(w)
	if word[0] != 'ь' and 'ьиа' not in word: 
		k.add(word)
print(len(k))