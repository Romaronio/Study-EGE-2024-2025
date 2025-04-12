for n in range(1, 13):
  s = bin(n)[2:]
  if n % 2 == 0:
    s = '10' + s
  if n % 2 == 1:
    s = '1' + s + '01'
  i = int(s, 2)
  print(i)
