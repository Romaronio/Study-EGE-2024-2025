def f(start, end, kom):
  print(kom)
  if start == end:
    return 1
  if start > end or start == 28 or 'BACA' in kom:
    return 0
  if start < end:
    return f(start + 2, end, kom = kom + 'A') + f(start + 3, end, kom = kom + 'B') + f(start * 2, end, kom = kom + 'C')

print(f(2, 40, ''))