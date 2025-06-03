i = (200 * 1_474_560) / (64 * 1050 * 460)
print(i)

P = 1050 * 460
Kol = 64
Scorost = 1_474_560
for i in range(1, 50):
    V1 = i * P
    V64 = V1 * 64
    t = V64 / Scorost
    if t < 200:
        print(i)

print(2 ** 9)