from itertools import *
def f(x, y, z, w):
    return ((y <= x) == (w <= (not(z)))) and (w or x)

for a in product([1, 0], repeat=2):
    table = [(0, 1, 1, 1), (1, 0, 1, 0), (a[0], 0, 0, a[1])]
    if len(set(table)) != 3:
        continue
    for i in permutations('xyzw'):
        if [f(**dict(zip(i, stroka))) for stroka in table] == [0, 1, 1]:
            print(i)
