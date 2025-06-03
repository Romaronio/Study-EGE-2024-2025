

for n in range(1, 1000):
  V1 = 2 * 128_000 * 16 * 120
  V_n = V1 * n
  if V_n / 10_467_554 <= 486:
    print(n)
