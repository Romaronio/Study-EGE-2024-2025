from fnmatch import *
for x in range(0, 10 ** 8, 31):
    if fnmatch(str(x), '123*578') and x % 31 == 0:
        print(x, x // 31)