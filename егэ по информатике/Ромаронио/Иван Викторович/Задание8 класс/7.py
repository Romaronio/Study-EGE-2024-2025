from itertools import permutations
k = set()
word = ''
for w in permutations('вентиль'):
	word = ''.join(w)
	if word[-1] != 'ь' and 'еьи' not in word and 'иье' not in word:
		k.add(word)
print(len(k))