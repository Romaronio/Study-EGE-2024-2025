from itertools import product
for i, w in enumerate(product(sorted('парус'), repeat=5), 1):
	word = ''.join(w)
	if word.count('у') <= 1 and 'аа' not in word:
		print(i)
