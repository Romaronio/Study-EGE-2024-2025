from math import *
N = 10 + 52 + 458
i = ceil(log2(N))
for L in range(1, 1000):
    V1 = ceil((i * L) / 8)
    if V1 * 862 <= 276 * 2 ** 10:
        print(L)

