from itertools import product
k = set()
for w in product('воробей', repeat=	5):
	word = ''.join(w)

	if word.count('й') < 2 and word[0] != 'й' and word[-1] != 'й' and 'ей' not in word and 'йе' not in word: 
		k.add(word)
print(len(k))