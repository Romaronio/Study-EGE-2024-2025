def div(x):
  d = set()
  for i in range(2, int(x ** 0.5) + 1):
    if x % i == 0:
      d.add(i)
      d.add(x // i)
  return sorted(d)

for x in range(250200, 251000):
  d = div(x)
  if len(d) >= 2:
    m = max(d) + min(d)
    if m % 123 == 17:
      print(x, m)