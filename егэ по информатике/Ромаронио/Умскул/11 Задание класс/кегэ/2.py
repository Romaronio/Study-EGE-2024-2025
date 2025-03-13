from math import *
L = 10
n = 26 + 26 + 10
i = ceil(log2(n))
V1 = ceil((L * i) / 8)
V30 = V1 * 30
Vobs = 870
Vdop = Vobs - V30
print(Vdop / 30)