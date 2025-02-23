from math import *
for n in range(1, 10000):
  s = 261
  i = ceil(log2(n))
  V1 = ceil((i * s) / 8)
  V252500 = (V1 * 252500) / (1024 ** 2)
  if V252500 > 31:
    print(n)
    break