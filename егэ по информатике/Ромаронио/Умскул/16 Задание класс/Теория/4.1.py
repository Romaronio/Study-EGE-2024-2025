def f(n):
  if n == 1:
    return 1
  if n > 1 and n % 2 == 0:
    return f(n-1) + 7
  if n > 1 and n % 2 != 0:
    return f(n-2) + 4 * n
print(f(100))