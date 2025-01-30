from itertools import product
s = 0
word = [''.join(w) for w in product('аоу', repeat=5)]
s = word.index('уауау') - word.index('оуоуа') + 1
print(s)