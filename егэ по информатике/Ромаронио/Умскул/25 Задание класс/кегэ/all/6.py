def div(x):
  d = set()
  for i in range(2, int(x ** 0.5) + 1):
    if x % i == 0:
      d.add(i)
      d.add(x // i)
  return sorted(d)


for x in range(850_001, 850_100):
  d = div(x)
  if len(d) == 0 or len(d) == 1:
    continue
  if (max(d) - min(d)) % 3 == 0:
    print(x, max(d) - min(d))

