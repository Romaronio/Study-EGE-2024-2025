from math import *
for n in range(1, 10000):
  s = 10 + 26 + 232
  i = ceil(log2(s))
  V1 = ceil(((i * n) / 8))
  V760 = V1 * 760 // 1024
  if V760 > 140:
    print(n)
    break
