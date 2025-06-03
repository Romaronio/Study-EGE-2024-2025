from itertools import *
k = 0
for i in product(['С', 'Г', 'С', 'С', 'Г', 'С', 'С'], repeat=6):
  slovo = ''.join(i)
  if slovo[0] != 'Г' and slovo[-1] != 'С':
    k += 1

print(k)