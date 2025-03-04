def div(x):
  d = set()
  for i in range(1, int(x ** 0.5) + 1):
    if x % i == 0:
      d.add(i)
      d.add(x // i)
  return sorted(d)

for x in range(333555, 778000):
  d = [i for i in div(x) if 10 <= i <= 99]
  if len(d) == 35:
    print(x, min(d), max(d))