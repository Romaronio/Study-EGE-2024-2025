def f(n):
  if n == 1:
    return 3
  if n > 1:
    return 5 * f(n - 1)

print(f(10 ** 12 + 10) / 25 ** 5 * 10 ** 11)