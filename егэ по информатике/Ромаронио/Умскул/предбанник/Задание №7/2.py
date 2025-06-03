P = 1920 * 1080
V1 = 4096 * 2 ** 13


for i in range(1, 40):
    if V1 > i * P:
        print(i)