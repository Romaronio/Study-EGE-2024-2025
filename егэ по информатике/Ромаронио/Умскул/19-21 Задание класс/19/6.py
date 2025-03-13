def g(s, p, end):
  if s <= 19:
    return p in end
  if p > max(end):
    return False
  h = [g(s - 1, p + 1, end)]
  if s % 3 == 0:
    h.append(g(s // 3, p + 1, end))
  else:
    h.append(g(s - 2, p + 1, end))
  if s % 5 == 0:
    h.append(g(s // 5, p + 1, end))
  else:
    h.append(g(s - 3, p + 1, end))
  return any(h) if (p + 1) % 2 == end[0] % 2 else all(h)


for s in range(20, 100):
  if g(s, 0, [2]):
    print(s, '------------ 19 ------------')

for s in range(20, 200):
  if g(s, 0, [3]) and not(g(s, 0, [1])):
    print(s, '------------ 20 ------------')

for s in range(20,100):
  if g(s,0,[2, 4]) and not g(s, 0, [2]):
    print(s,'------------ 21 ------------')

