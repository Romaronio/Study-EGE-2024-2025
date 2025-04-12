m = []
for n in range(1, 10000):
  n = n - bin(n)[2:].count('0')
  s = bin(n)[2:]
  if s.count('0') == 3:
    s = '000' + s
  if s.count('0') == 2:
    s = '001' + s
  if s.count('0') == 1:
    s = '011' + s
  if s.count('0') == 0:
    s = '111' + s
  m.append(int(s, 2))
  m.sort()
  for k in m:
    if k > 224:
      print(k, s)
      break

