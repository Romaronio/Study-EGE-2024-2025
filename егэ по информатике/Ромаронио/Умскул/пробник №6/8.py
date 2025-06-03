from itertools import *
k = 0
for i in product('SOUTH', repeat=6):
  if i.count('U') == 1:
    if i[0] != 'S' and i[-1] != 'H':
      k += 1

print(k)