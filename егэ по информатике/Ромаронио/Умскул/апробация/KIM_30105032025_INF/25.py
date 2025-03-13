def Del(x):
  d = set()
  for i in range(2, int((x ** 1/2))):
    if x % i == 0:
      d.add(i)
      d.add(x // i)
  return sorted(d)
for x in range(700_000, 700_100):
  f = Del(x)
  if len(f) == 0:
    m = 0
  else:
    m = f[0] + f[-1]
  if m % 10 == 4:
    print(x, m)
