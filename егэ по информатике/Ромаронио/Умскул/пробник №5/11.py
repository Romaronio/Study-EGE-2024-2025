from math import *
L = 13
alfa = 26 * 2 + 20
i = int(log2(alfa))
V1 = L * i

V50 = ceil((V1 * 50) / 8)

print(V50)

print((1800 - V50) / 50)
