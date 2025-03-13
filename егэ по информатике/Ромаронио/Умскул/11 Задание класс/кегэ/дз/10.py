from math import *
N = 10 + 52 + 458
V1 = int((276 * 1024) / 862)
print(V1)
i = ceil(log2(N))
L = int(V1 * 8 / i)
print(L)