from math import *
i = int(log2(1032))
# V385 = 136 * 2 ** 13
#
# for n in range(1, 1000):
#     V1 = n * i
#     if V1 * 385 < V385:
#         print(n)

print(264 * i * 385 < 136 * 8 * 1024)
