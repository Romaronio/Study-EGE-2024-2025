def three(x):
  res = ''
  while x:
    res = str(x % 3) + res
    x = x // 3
  return res


for x in range(0, 2031):
  s = 3 ** 100 - x
  m = three(s)
  if m.count('0') == 1:
    print(x)

print(three(3 ** 100 - 1828))