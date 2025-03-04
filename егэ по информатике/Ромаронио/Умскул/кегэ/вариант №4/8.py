from itertools import *
A = []
for a in product(['У','Д', 'А', 'Ч'], repeat=5):
  if a[0] in 'УА':
    A.append(a)
for i, a in enumerate(A):
  print(i, A[i])
