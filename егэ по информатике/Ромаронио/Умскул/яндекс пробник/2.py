from itertools import product,permutations


def f(x, y, w):
  return ((x <= y) and (w or (not(w))))

for a in product([1, 0], repeat=3):
  table = [(1, 1, 0), (a[0], 1, a[1]), (1, 0, 1), (1, a[2], 1)]
  if len(set(table)) != len(table):
    continue
  for i in permutations('xyw'):
    if [f(**dict(zip(i, a))) for a in table] == [0,0,1,1]:
      print(i)