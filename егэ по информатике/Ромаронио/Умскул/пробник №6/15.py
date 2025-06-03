for A in range(1, 1000):
  A_podoshel = 1
  for x in range(1, 1000):
    for y in range(1, 1000):
      if (((x ** 2 - 19 * x - 89 < 0) or (y ** 2 + 17 * y - 10 < 0)) <= (x < 2 * A)) == 0:
        A_podoshel = 0
        break
    else:
      if A_podoshel == 0:
        break
  else:
    print(A)

