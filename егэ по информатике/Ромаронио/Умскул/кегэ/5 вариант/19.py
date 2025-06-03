# def g(s, p, end):
#   if s == 42 and p in end:
#     return True
#   if s != 42 and p == max(end):
#     return False
#   if s == 42 and p not in end:
#     return False
#   h = [g(s + 1, p + 1, end), g(s + 3, p + 1, end), g(s + 7, p + 1, end)]
#   return any(h) if (p + 1) % 2 == end[0] % 2 else all(h)
#
# for s in range(1, 100):
#   if g(s, 0, [2]) and not(g(s, 0, [1])):
#     print(s)


def g(s, p, end):
  if s == 42 and p == end:
    return True
  if s != 42 and p == end:
    return False
  if s == 42 and p != end:
    return False
  if (p + 1) % 2 == end % 2:
    return g(s + 1, p + 1, end) or g(s + 3, p + 1, end) or g(s + 7, p + 1, end)
  else:
    return g(s + 1, p + 1, end) and g(s + 3, p + 1, end) and g(s + 7, p + 1, end)

for s in range(1, 100):
  if g(s, 0, 2):
    print(s)
