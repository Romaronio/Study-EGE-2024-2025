from fnmatch import *
for x in range(0, 10 ** 8, 63):
  if fnmatch(str(x), '134?3?') and x % 63 == 0:
    print(x, x // 63)