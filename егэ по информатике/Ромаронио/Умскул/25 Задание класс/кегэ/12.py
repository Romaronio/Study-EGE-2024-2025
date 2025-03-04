def div(x):
  d = set()
  for i in range(1, int(x ** 0.5) + 1):
    if x % i == 0:
      d.add(i)
      d.add(x // i)
  return sorted(d)


def simple(x):
  return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

for x in range(4202865, 4202923 + 1):
  d = div(x)
  if simple(x):
    print(d)