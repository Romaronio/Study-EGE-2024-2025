from fnmatch import *
for x in range(0, 10 **9, 169):
  if fnmatch(str(x), '345*789?'):
    print(x, x // 1692)