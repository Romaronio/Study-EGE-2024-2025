from math import *
L = 101
N = 10 + 4090
i = ceil(log2(N))
V1 = ceil((L * i) / 8)
v2048 = (V1 * 2048) / 2 ** 10
print(v2048)