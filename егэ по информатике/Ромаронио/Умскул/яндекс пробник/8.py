def seven(s):
  seven = ''
  while s > 0:
    seven += str(s % 7)
    s = s // 7
  return seven
m = 0
for i in range(1, 200000):
  s = seven(i)
  if len(s) == 6:
    if s.count('0') == 1:
      k = s.count('2')
      k += s.count('4')
      k += s.count('6')
      if k % 2 == 0:
        m += 1
print(m)