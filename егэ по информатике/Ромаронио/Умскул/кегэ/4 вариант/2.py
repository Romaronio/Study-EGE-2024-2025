from itertools import *
def f(x, y, z, w):
  return (((not(x)) and w) <= y) and (y <= (z and (not(y))))


for a in product([0,1], repeat=4):
  table = [(0, a[0], 1, 1), (1, 0, a[1], 0), (1, a[2], a[3], 0)]
  if len(set(table)) != 3:
    continue
  for i in permutations('xyzw'):
    if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 1]:
      print(i)