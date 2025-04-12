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
  if g(s, 0, [3]) and not(g(s, 0, [1])):
    print(s)



# def g(s, p, end):
#   if s <= 19 and p == end:
#     return True
#   if s <= 19 and p != end:
#     return False
#   if s > 19 and p == end:
#     return False
#   if (p + 1) % 2 == end % 2:
#     return g(s - 2, p + 1, end) or g(s - 5, p + 1, end) or g(int(s / 3), p + 1, end)
#   else:
#     return g(s - 1, p + 1, end) and g(s - 5, p + 1, end) and g(int(s / 3), p + 1, end)
#
# for s in range(1, 1000):
#   if g(s, 0, 2) and not(g(s, 0, 1)):
#     print(s)