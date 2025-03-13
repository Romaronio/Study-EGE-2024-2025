from math import *
L = 9
N = 10 + 26 + 26 + 6
i = ceil(log2(N))
V1 = ceil(L * i / 8)
Vobs = 500
V_1 = 500 / 20
print(V1, V_1)
Vdop = V_1 - V1
print(Vdop)

