for n in range(2, 11):
  ost = ''
  s = 364
  while s:
    ost = str(s % n) + ost
    s = s // n
  print(ost)