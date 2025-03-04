for n in range(2, 1000):
  s = bin(n)[2:]
  s = s + s[1]
  if s.count('1') % 2 == 0:
    s = s + '0'
  else:
    s = s + '1'
  if s.count('1') % 2 == 0:
    s = s + '1'
  else:
    s = s + '0'

  if int(s, 2) > 160:
    print(n, int(s, 2))