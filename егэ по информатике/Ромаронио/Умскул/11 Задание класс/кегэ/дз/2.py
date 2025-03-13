from math import *
L = 7
N = 12
i = ceil(log2(N))
V1 = ceil((L * i) / 8)
V1_dop = V1 + 15
VObs = V1_dop * 150
print(VObs)
