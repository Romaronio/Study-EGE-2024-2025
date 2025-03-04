def f(x, y, z, w):
  return (not((x == y) or (x == w))) or z or (not(y <= w))
from itertools import *
for a in product([0, 1], repeat=9):
  table = [(1, 0, 0, a[0]), (a[1], a[2], a[3], a[4]), (1, 1, a[5], a[6]), (a[7], 0, 1, a[8])]
  if len(set(table)) != 4:
    continue
  for i in permutations('xyzw'):
    if [f(**dict(zip(i, stroka))) for stroka in table] == [0, 0, 0, 0]:
      print(i)