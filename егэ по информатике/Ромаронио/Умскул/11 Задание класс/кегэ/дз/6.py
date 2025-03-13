from math import *
L_lich = 11
N_lich = 15 + 10
i_lich = ceil(log2(N_lich))
V_lich = ceil((i_lich * L_lich) / 8)

L_pod = 8
N_pod_1 = 30
N_pod_2 = 10
i_pod_1 = ceil(log2(N_pod_1))
i_pod_2 = ceil(log2(N_pod_2))

V_pod_1 = ceil((5 * i_pod_1))
V_pod_2 = ceil((3 * i_pod_2))

V_pod = ceil((V_pod_1 + V_pod_2) / 8)

Vobs1 = 30

V = Vobs1 - (V_pod + V_lich)
print(V)