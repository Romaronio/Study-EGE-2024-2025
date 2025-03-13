from math import *
L = 11
N = 26 * 2 + 10
i = log2(N)
V1 = ceil(L * i / 8) + 13
Vobs = 1024
K_pol = Vobs / V1
print(K_pol)