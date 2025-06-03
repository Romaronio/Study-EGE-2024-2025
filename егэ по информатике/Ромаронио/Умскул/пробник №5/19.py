# def g(s, p, end):
#   if s >= 46 and p == end:
#     return True
#   if s < 46 and p == end:
#     return False
#   if s >= 46 and p != end:
#     return False
#   if (p + 1) % 2 == end % 2:
#     return g(s * 2, p + 1, end) or g(s + 2, p + 1, end)
#   else:
#     return g(s * 2, p + 1, end) and g(s + 2, p + 1, end)
#
# for s in range(1, 46):
#   if g(s, 0, 2):
#     print(s)


def g(s, p, end):
  if s >= 46:
    return p in end
  if s < 46 and p == max(end):
    return False
  h = [g(s * 2, p + 1, end), g(s + 2, p + 1, end)]
  return any(h) if (p + 1) % 2 == end[0] % 2 else all(h)

for s in range(1, 46):
  if g(s, 0, [2, 4]) and not(g(s, 0, [2])):
    print(s)