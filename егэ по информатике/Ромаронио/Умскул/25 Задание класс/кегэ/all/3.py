def div(x):
  d = set()
  for i in range(2, int(x ** 1/2) + 1):
    if x % i == 0:
      d.add(i)
      d.add(x // i)
  return sorted(d)


for x in range(81234, 134690):
  d = div(x)
  if len(d) == 3:
    print(d)