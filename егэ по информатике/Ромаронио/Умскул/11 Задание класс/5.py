from math import *
for n in range(1, 10000):
  kol_vo_nomerov = 8192
  i = ceil(log2(n))
  V1 = ceil((205 * i) / 8)
  V8192 = (V1 * 8192) / 1024
  if V8192 <= 899:
    print(n)

