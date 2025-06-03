from itertools import *
k = 0
for i in product('гссгсс', repeat=5):
  if i[0] != 'г' and i[-1] != 'с':
    k += 1

print(4 * 6 * 6 * 6 * 2)
print(k)