def f(n):
  if n > 15:
    return n * 2
  if n <= 15:
    return 2 * f(n + 2) + 4 * n
print(f(7))