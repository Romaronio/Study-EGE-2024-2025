from math import *
for n in range(1, 10000):
  i = ceil(log2(n))
  s = 317
  V1 = ceil((i * s) / 8)
  V487321 = (V1 * 487321) / 2 ** 20
  if V487321 > 130:
    print(n)
    break
