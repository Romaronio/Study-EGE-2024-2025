def f(x, y):
  return (2 * y + 3 * x < a) or (x + y > 40)
for a in range(0, 200):
    if all(f(x, y) for y in range(1,1000) for x in range(1,1000)) == 1:
      print(a)
