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
    return g(s + 1, t, p + 1, end) or g(s, t + 1, p + 1, end) or g(s * 2, t, p + 1, end) or g(s, t * 2, p + 1, end)

t = 7
for s in range(1, 74):
  if g(s, t, 0, 2):
    print(s, t)
    print(19 * 2 * 2 + 7)