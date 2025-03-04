def g(s, x, p, end):
  if s + x >= 30 and p in end:
    return True
  if s + x < 30 and p == max(end):
    return False
  if s + x > 30 and p not in end:
    return False
  if (p + 1) % 2 == end[0] % 2:
    return g(s + 3, x, p + 1, end) or g(s * 2, x, p + 1, end) or g(s, x + 3, p + 1, end) or g(s, x * 2, p + 1, end)
  else:
    return g(s + 3, x, p + 1, end) and g(s * 2, x, p + 1, end) and g(s, x + 3, p + 1, end) and g(s, x * 2, p + 1, end)

x = 5
for s in range(1, 30):
  if g(s, x, 0, [2, 4]):
    print(s)