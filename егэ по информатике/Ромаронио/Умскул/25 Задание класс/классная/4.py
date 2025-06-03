from fnmatch import *
for x in range(0, 10 ** 8, 343):
  if fnmatch(str(x), '51?32*8'):
    print(x, x // 343)