def F(n):
  if n == 1:
    return 1
  if n > 1 and n % 2 == 0:
    return F(n - 1) + 3
  if n > 1 and n % 2 == 1:
    return F(n - 3) + 2 * n

print(F(50))
