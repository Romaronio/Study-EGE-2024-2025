def f(start, end):
  if start == end:
    return 1
  if start > end or start == 12:
    return 0
  if start < end:
    return f(start + 2, end) + f(start * 2, end) + f(start * 4, end)

print(f(6, 16) * f(16, 48))
