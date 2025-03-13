def g(s, t, p, end):
  if s + t >= 81 and p == end:
    return True
  if s + t >= 81 and p != end:
    return False
  if s + t <= 81 and p == end:
    return False
  if (p + 1) % 2 == end % 2:
    return g(s + 1, t, p + 1, end) or g(s, t + 1, p + 1, end) or g(s * 2, t, p + 1, end) or g(s, t * 2, p + 1, end)
  else:
    return g(s + 1, t, p + 1, end) and g(s, t + 1, p + 1, end) and g(s * 2, t, p + 1, end) and g(s, t * 2, p + 1, end)

t = 7
for s in range(1, 74):
  if g(s, t, 0, 3) and not(g(s, t, 0, 1)):
    print(s, t)