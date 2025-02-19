for a in range(1, 100):
  a_podoshel = 1
  for x in range(1, 100):
    for y in range(1,100):
      if ((2 * y + x > 37) or (a > x) or (a > y)) == 0:
        a_podoshel = 0
  if a_podoshel == 1:
    print(a)
