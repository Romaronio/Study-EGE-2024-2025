from fnmatch import *
for x in range(1, 100_000):
    if fnmatch(str(x), '1?7*') and x % 134 == 0:
        print(f'{x:b}'.count('1'))