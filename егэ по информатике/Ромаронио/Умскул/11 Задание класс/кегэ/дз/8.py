from math import *
L = 20
N = 2 + 7
i = ceil(log2(N))
V_par = ceil((i * L) / 8)
V1 = V_par + 4
Vobs = 6 * 1024
V_1 = Vobs / 192
Vdop = V_1 - V1
print(Vdop)