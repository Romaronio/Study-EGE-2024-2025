from fnmatch import *
for x in range(0, 10 ** 8, 98):
    if fnmatch(str(x), '12*678?') and x % 98 == 0:
        print(x, x // 98)