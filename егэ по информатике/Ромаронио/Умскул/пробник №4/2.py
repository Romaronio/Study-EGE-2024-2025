from itertools import *
def f(x, y, z, w):
  return ((y <= z) <= (x and y)) and (x <= w)
for a in product([1, 0], repeat=4):
  table = [(0, 0, 0, a[0]), (0, 0, a[1], 1), (0, a[2], a[3], 1)]
  if len(set(table)) != 3:
    continue
  for i in permutations('xyzw'):
    if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 1]:
      print(i)

