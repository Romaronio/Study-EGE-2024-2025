from itertools import product
word = [''.join(w) for w in product('дкмо', repeat=5)]
sum = word.index('комод') - word.index('домок') + 1
print(sum)
