for n in range(1, 1000):
  s = bin(n)[2:]
  s = s + str(s.count('1') % 2)
  s = s + str(s.count('1') % 2)
  if int(s, 2) > 1096:
    print(n, int(s, 2))