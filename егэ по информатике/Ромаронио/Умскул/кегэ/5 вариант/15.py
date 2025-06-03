def Deli(n, m):
  return n % m == 0

for a in range(1, 1000):
  for x in range(1, 10000):
    if ((not(Deli(x, a))) <= ((Deli(x, 14)) <= (not(Deli(x, 4))))) == 0:
      break
  else:
    print(a)

