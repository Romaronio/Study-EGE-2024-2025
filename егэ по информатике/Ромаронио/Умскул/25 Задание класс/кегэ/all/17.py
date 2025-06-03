def simple(x):
  return x > 0 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

for x in range(152, 165):
  if simple(x):
    print(x ** 4, x ** 3)
