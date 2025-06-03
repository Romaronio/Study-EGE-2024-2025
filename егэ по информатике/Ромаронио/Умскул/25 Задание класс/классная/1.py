from fnmatch import *
for x in range(61, 10 ** 8, 61):
  if fnmatch(str(x), '23456??8') and x % 61 == 0:
    print(x, x // 61)
