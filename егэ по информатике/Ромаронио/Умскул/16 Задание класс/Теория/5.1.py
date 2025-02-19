def f(n):
  if n <= 4:
    return 0
  if n % 4 == 0 and n > 4:
    return f(n-1) + 3 * n
  if n % 4 != 0 and n > 4:
    return f(n - (n % 4)) + 8 * n - 2
print(f(43))