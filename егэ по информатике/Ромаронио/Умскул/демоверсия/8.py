from itertools import *
alfa = '0123456789ab'
k = 0
for i in permutations(alfa, r=5):
  if i.count('7') != 1:
    continue
  elif i.count('9') + i.count('a') + i.count('b') > 3:
    continue
  k += 1 
print(k)