from itertools import permutations
k = set()
for x in permutations(sorted('хочу в вуз')):
	word = ''.join(x)
	if word[0] != ' ' and word[-1] != ' ' and '  ' not in word and word[0] != 'у' and ' у' not in word:
		k.add(word)
print(len(k) - 1)
