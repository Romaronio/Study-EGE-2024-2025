from itertools import permutations
k = set()
for w in permutations('хочу сотку'):
	word = ''.join(w)
	if word[0] != 'у' and word[0] != ' ' and word[-1] != ' ' and ' у' not in word:
		k.add(word)
print(len(k) - 1)
