from itertools import *


def f(x, y, z, w):
  return ((w <= y) <= x) or (not(z))

for a in product([1, 0], repeat=7):
  table = [(a[0], a[1], 1, a[2]), (a[3], 0, a[4], a[5]), (a[6], 1, 0, 0)]
  if len(set(table)) != 3:
    continue

  for i in permutations('xyzw'):
    if [f(**dict(zip(i, stroka))) for stroka in table] == [0, 0, 0]:
      print(i)