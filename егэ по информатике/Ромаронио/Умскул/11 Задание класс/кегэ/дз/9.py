from math import *
L = 101
N = 10 + 4090
i = ceil(log2(N))
V1 = ceil((L * i) / 8)
V2048 = (V1 * 2048) / 1024
print(V2048)
