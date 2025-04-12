for n in range(1, 10000):
  s = bin(n)[2:]
  if s.count('1') % 2 == 0:
    s += '0'
  else:
    s += '1'
  if s.count('1') % 2 == 0:
    s += '0'
  else:
    s += '1'
  if int(s, 2) > 22222:
    print(int(s, 2))
    break