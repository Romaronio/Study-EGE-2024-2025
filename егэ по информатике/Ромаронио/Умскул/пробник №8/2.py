from itertools import *
def f(x, y, z, w):
    return ((w or x) and ((y <= (not(x))) == (x <= z)) and x)

for a in product([1, 0], repeat=4):
    table = [(0, 1, a[0], 1), (1, a[1], a[2], 1), (a[3], 0, 1, 0)]
    if len(set(table)) != 3:
        continue
    for i in permutations('xyzw'):
        if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 1]:
            print(i)