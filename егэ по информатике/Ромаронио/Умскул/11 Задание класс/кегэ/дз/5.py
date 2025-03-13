from math import *
Nnom = 101
inom = log2(Nnom)
Vnom = ceil((1 * inom) / 8)
L = 11
Nlich = 52 + 10
ilich = log2(Nlich)
VLich = ceil((L * ilich) / 8)
Vdop = 28 - (VLich + Vnom)
print(Vdop)
