from itertools import *
def f(x, y, z, w):
  return ((x and (not(y))) and (w <= z))

for a in product([0, 1], repeat=5):
  table = [(0, a[0], a[1], 1), (0, a[2], 1, 1), (1, a[3], a[4], 1)]
  if len(set(table)) != 3:
    continue
  for i in permutations('xyzw'):
    if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 1]:
      print(i)
