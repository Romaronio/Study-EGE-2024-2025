for n in range(1, 1000):
  s = bin(n)[2:]
  if n % 2 == 0:
    s = '1' + s + '10'
  else:
    s = '11' + s + '0'
  if int(s, 2) > 260:
    print(int(s, 2))
    break