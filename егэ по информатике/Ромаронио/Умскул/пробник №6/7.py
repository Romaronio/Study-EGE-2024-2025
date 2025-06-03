from math import *
N = 32768
i = log2(N)
S = 1024 * 768

V = i * S
V1 = (V / 2 ** 13) + 3
V30 = (V1 * 30) / 1024
print(V30)
