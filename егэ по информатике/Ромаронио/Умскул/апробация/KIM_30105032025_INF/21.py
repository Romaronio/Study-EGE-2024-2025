def g(s, t, p, end):
  if s + t >= 81 and p in end:
    return True
  if s + t >= 81 and p not in end:
    return False
  if s + t <= 81 and p == max(end):
    return False
  if (p + 1) % 2 == end[0] % 2:
    return g(s + 1, t, p + 1, end) or g(s, t + 1, p + 1, end) or g(s * 2, t, p + 1, end) or g(s, t * 2, p + 1, end)
  else:
    return g(s + 1, t, p + 1, end) and g(s, t + 1, p + 1, end) and g(s * 2, t, p + 1, end) and g(s, t * 2, p + 1, end)

t = 7
for s in range(1, 74):
  if g(s, t, 0, [2, 4]) and not(g(s, t, 0, [2])):
    print(s, t)