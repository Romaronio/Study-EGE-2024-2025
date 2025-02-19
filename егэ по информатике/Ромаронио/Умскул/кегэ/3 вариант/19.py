# def g(s, p, end):
#   if s >= 58 and p == end:
#     return True
#   if s < 58 and p == end:
#     return False
#   if s >= 58 and p != end:
#     return False
#   if ((p + 1) % 2) == end % 2:
#     return g(s + 1, p + 1, end) or g(s + 4, p + 1, end) or g(s * 2, p + 1, end)
#   else:
#     return g(s + 1,p + 1,end) and g(s + 4,p + 1,end) and g(s * 2,p + 1,end)
#
# for s in range(100):
#   if not(g(s, 0, 1)) and g(s, 0, 2):
#     print(s)

# def g(s, p, end):
#   if s >= 58 and p == end:
#     return True
#   if s < 58 and p == end:
#     return False
#   if s >= 58 and p != end:
#     return False
#   if ((p + 1) % 2) == end % 2:
#     return g(s + 1, p + 1, end) or g(s + 4, p + 1, end) or g(s * 2, p + 1, end)
#   else:
#     return g(s + 1,p + 1,end) and g(s + 4,p + 1,end) and g(s * 2,p + 1,end)
#
# for s in range(100):
#   if g(s, 0, 3):
#     print(s)


def g(s, p, end):
  if s >= 58 and p in end:
    return True
  if s < 58 and p == max(end):
    return False
  if s >= 58 and p not in end:
    return False
  if ((p + 1) % 2) == end[0] % 2:
    return g(s + 1, p + 1, end) or g(s + 4, p + 1, end) or g(s * 2, p + 1, end)
  else:
    return g(s + 1,p + 1,end) and g(s + 4,p + 1,end) and g(s * 2,p + 1,end)

for s in range(100):
  if g(s, 0, [2, 4]):
    print(s)

