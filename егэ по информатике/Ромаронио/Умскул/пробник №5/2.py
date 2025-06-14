from itertools import *

def f(x, y, z, w):
  return (x and (not(y))) or (x == z) or (not(w))


for a in product([0,1], repeat=4):
  table = [(a[0], a[1], 0, 0), (1, 1, 1, 0), (1, 0, a[2], a[3])]
  if len(set(table)) != 3:
    continue
  for i in permutations('xyzw'):
    if [f(**dict(zip(i, stroka))) for stroka in table] == [0, 0, 0]:
      print(i)