def div(x):
  d = set()
  for i in range(1, int(x ** 0.5) + 1):
    if x % i == 0:
      d.add(i)
      d.add(x // i)
  return sorted(d)

for x in range(250000, 250200 + 1):
  d = [i for i in div(x) if i % 2 == 0]
  if len(d) == 6:
    print(d[4], d[5])








