def g(x, y, p, end):
  if x + y >= 234 and p == end:
    return True
  if x + y <= 234 and p == end:
    return False
  if x + y >= 234 and p != end:
    return False
  if (p + 1) % 2 == end % 2:
    return g(x + 1, y, p + 1, end) or g(x, y + 1, p + 1, end) or g(x * 5, y, p + 1, end) or g(x, y * 5, p + 1, end)
  else:
    return g(x + 1, y, p+1, end) and g(x, y + 1, p+1, end) and g(x * 5, y, p+1, end) and g(x, y * 5, p+1, end)
x = 7
for y in range(1, 226):
  if (not(g(x, y, 0, 1))) and g(x, y, 0, 3):
    print(y)