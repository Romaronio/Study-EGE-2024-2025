for n in range(1, 1000):
  s = bin(n)[2:]
  if n % 2 == 0:
    s = s + bin(s.count('1'))[2:]
  else:
    s = '1' + s + '00'
  if int(s, 2) > 215:
    print(n, int(s, 2))