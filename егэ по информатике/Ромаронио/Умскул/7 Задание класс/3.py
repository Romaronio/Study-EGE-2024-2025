t = 120
nu1 = 64_000
i1 = 24
nu2 = 20_000
i2 = 8
V1 = 2 * nu1 * i1 * t
V2 = 1 * nu2 * i2 * t
res = ((V1 - V2) * 180) // 2 ** 13
print(res)