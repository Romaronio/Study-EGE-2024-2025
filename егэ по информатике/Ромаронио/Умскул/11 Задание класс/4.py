from math import *
for a in range(1, 10000):
  l = 191
  i = ceil(log2(a))
  n = 191
  V1 = ceil((n * i) / 8)
  V131 = (V1 * 131072) / 2 ** 20
  if V131 > 22:
    print(a)
    break
