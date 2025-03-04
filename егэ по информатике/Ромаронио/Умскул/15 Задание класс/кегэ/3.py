for a in range(1, 1000):
  for x in range(1, 10000):
    if ((x & 41 == 0) <= ((x & 119 != 0) <= (x & a != 0))) == 0:
      break
  else:
    print(a)