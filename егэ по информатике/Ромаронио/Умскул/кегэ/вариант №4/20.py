def g(s, x, p, end):
  if s + x >= 30 and p == end:
    return True
  if s + x < 30 and p == end:
    return False
  if s + x > 30 and p != end:
    return False
  if (p + 1) % 2 == end % 2:
    return g(s + 3, x, p + 1, end) or g(s * 2, x, p + 1, end) or g(s, x + 3, p + 1, end) or g(s, x * 2, p + 1, end)
  else:
    return g(s + 3, x, p + 1, end) and g(s * 2, x, p + 1, end) and g(s, x + 3, p + 1, end) and g(s, x * 2, p + 1, end)

x = 5
k = 0
for s in range(1, 30):
  if g(s, x, 0, 3) or g(s, x, 0, 1):
    k += 1

print(k)