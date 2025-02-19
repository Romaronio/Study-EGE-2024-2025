def f(n):
  if n < 2:
    return 1
  if n >= 2:
    return f(n - 1) * (n + 5)
print(f(5))