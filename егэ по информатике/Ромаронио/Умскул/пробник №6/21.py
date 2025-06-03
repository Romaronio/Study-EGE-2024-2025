def g(s, p, end):
  if s >= 88:
    return p in end
  if p > max(end):
    return False
  h = [g(s + 2, p + 1, end), g(s * 2 - 1, p + 1, end)]
  return any(h) if (p + 1) % 2 == end[0] % 2 else all(h)

for s in range(1, 100):
  if g(s, 0, [2, 4]) and not(g(s, 0, [2])):
    print(s)
