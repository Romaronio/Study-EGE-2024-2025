from itertools import *
k = 0
for i in permutations(['с', 'г', 'с', 'с', 'г', 'г', 'с', 'г', 'г'], r=6):
  res = ''
  for s in i:
    res = res + s
  print(res)
  if 'сс' not in res and 'гг' not in res:
    k += 1

print(k)