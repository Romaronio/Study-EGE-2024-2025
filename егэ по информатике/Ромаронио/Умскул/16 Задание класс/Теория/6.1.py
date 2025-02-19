def f(n):
    if n == 2:
      return 1
    if n > 2:
      return 3 * f(n - 1) + 4 * g(n - 1) - n * 2 + 4
def g(n):
  if n == 2:
    return 1
  if n > 2:
    return 4 * f(n - 1) + 3 * g(n - 1) + 6
print(f(8) + g(8))