P = 1280 * 720
i = 13
t = 280
Vs = 1_474_560
for x in range(1, 100):
    if (P * i * x) / Vs < 280:
        print(x)