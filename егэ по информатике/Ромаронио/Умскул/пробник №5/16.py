def f(n):
  if n <= 3:
    return 1
  if n % 2 == 0 and n > 3:
    return f(n / 5 - 3)
  if n % 2 == 1 and n > 3:
    return n * n * n

for n in range(1, 100):
  if f(n) > 559:
    print(n, f(n))