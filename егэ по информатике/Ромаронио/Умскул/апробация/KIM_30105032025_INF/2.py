# print('x y z w')
# for x in range(2):
#   for y in range(2):
#     for z in range(2):
#       for w in range(2):
#         if ((not(x <= y)) or (z <= w) or (not(z))) == 0:
#           print(x, y, z, w)

def f(x, y, z, w):
  return (not(x <= y)) or (z <= w) or (not(z))
from itertools import *
for a in product([0, 1], repeat=7):
  table = [(a[0], 0, a[1], 0), (1, a[2], a[3], a[4]), (0, 1, a[5], a[6])]
  if len(set(table)) != 3:
    continue

  for i in permutations('xyzw'):
    if [f(**dict(zip(i, stroka))) for stroka in table] == [0, 0, 0]:
      print(i)
