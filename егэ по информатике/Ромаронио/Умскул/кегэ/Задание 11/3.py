from math import *
for l in range(1, 10000):
  n = 10 + 26 + 496
  i = ceil(log2(n))
  V1 = ceil((l * i) / 8)
  V725 = (V1 * 725) / 1024
  if V725 > 353:
    print(l)
    break