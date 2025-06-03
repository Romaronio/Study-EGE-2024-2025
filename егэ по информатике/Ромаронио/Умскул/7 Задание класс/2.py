V1_nach = 3840 * 2160 * 18
V1_con = 2560 * 1440 * 6

res = ((V1_nach - V1_con) * 2048) / 2 ** 23
print(res)

