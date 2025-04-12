# def g(s, p, end):
#   if s <= 19 and p in end:
#     return True
#   if s <= 19 and p != end:
#     return False
#   if s > 19 and p == max(end):
#     return False
#   h = [g(s - 2, p + 1, end), g(s - 5, p + 1, end), g(int(s / 3), p + 1, end)]
#   return any(h) if (p + 1) % 2 == end[0] % 2 else all(h)
#
# for s in range(1, 1000):
#   if g(s, 0, [2, 4]) and not(g(s, 0, [2])):
#     print(s)
# #

def g(s, p, end):
  if s <= 19 and p in end:
    return 1
  if s <= 19 and p != max(end):
    return False
  if s > 19 and p == max(end):
    return False
  h = [g(s - 2, p + 1, end), g(s - 5, p + 1, end), g(int(s / 3), p + 1, end)]
  return any(h) if (p + 1) % 2 == end[0] % 2 else all(h)

for s in range(1, 1000):
  if g(s, 0, [3]):
    print(s)