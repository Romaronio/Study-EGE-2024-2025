for n in range(1, 1000):
  s = bin(n)[2:]
  if s.count('1') % 2 == 0:
    s = '10' + s[2:] + '10'
  if s.count('1') % 2 == 1:
    s = '11' + s[2:] + '01'

  if int(s, 2) <= 390:
    print(n, int(s, 2))