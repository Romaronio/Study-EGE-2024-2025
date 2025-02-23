from math import *
for n in range(1, 10000):
  a = 10 + 52 + 1000
  i = ceil(log2(a))
  V1 = ceil((n * i) / 8)
  V777 = 777 * V1 / 1024
  if V777 <= 276:
    print(n)