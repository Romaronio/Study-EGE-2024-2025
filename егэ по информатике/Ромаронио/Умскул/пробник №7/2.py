from itertools import *
def f(x, y, z, w):
    return (x and (not(y))) or (y == z) or (not(w))

for a in product([1, 0], repeat=5):
    table = [(a[0], 0, a[1], a[2]), (1, 0, a[3], 0), (1, a[4], 0, 0)]
    if len(set(table)) != 3:
        continue
    for i in permutations('xyzw'):
        if [f(**dict(zip(i, stroka))) for stroka in table] == [0, 0, 0]:
            print(i)
