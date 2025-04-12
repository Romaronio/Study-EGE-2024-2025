def f(A, B, x, y):
  return ((y <= 2 * x ** 2 - 12 * x + A -2) or (y <= -4 * x + B)) == (not(y <= ((x - 4) ** 2 + abs((x - 2) ** 2 - 16))))


for A in range(1, 100):
  for B in range(1, 100):
    for x in range(1, 100):
      for y in range(1, 100):
        if f(A, B, x, y) == 1:
          break
      if f(A,B,x,y) == 1:
        break
    if f(A, B, x, y) == 0:
      print(A, B)


