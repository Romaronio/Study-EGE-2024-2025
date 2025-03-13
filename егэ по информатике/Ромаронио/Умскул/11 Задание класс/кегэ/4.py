from math import *
L = 7
N = 26 + 26
i = ceil(log2(N))
V1 = ceil((L * i) / 8)
V2 = V1 + 12
k_pol = int(2048 / V2)
print(k_pol)
