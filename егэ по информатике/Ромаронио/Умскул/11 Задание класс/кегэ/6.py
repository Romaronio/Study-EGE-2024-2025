from math import *
# N = 52 + 10 + 1988
# i = ceil(log2(N))
# Vobs = 579 * 1024
# V1 = Vobs / 1974
# L = int(V1 / i * 8)
# print(L)



V1 = 579 * 1024 / 1974
i = ceil(log2(52 + 10 + 1988))
for L in range(1, 10000):
  if L == int(V1 / i * 8):
    print(L)