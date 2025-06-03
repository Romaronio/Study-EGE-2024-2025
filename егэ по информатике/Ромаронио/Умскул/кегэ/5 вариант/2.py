from itertools import *
def f(a, b, c, d):
  return (a <= b) and (c <= d) or (not(c))

table = [(1, 0, 1, 0), (0, 0, 1, 1), (0, 1, 1, 1), (1, 0, 1, 1)]
for i in permutations('abcd'):
  if [f(**dict(zip(i, stroka)))  for stroka in table] == [0, 0, 0, 0]:
    print(i)