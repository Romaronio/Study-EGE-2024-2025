from itertools import *
res_mas = []
for i in permutations('пескарь'):
  i = ''.join(i)
  if i[0] != 'ь':
    if 'ье' not in str(i):
      if 'ьа' not in str(i):
        if 'ьр' not in str(i):
          res_mas.append(i)
print(len(res_mas))