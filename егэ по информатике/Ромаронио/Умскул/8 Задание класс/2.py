from itertools import *
k = 0
for i in product(['С', 'С', 'Г', 'Г', 'С', 'Г'], repeat=5):
  m = ''.join(i)
  if m[0] not in 'Г' and m[-1] not in 'С':
    k += 1

print(k)

