from itertools import product
k = 0
for i, w in enumerate(product(sorted('глубина', reverse=True), repeat=6), 1):
	s = ''.join(w)
	for c in 'глубин':
		s = s.replace(c, '*')
	if i % 2 and 'а**а' in s and w.count('н') > 1:
		k += 1
print(k)
