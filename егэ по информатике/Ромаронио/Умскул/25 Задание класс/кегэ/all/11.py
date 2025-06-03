def div(x):
  d = set()
  for i in range(2, int(x ** 0.5) + 1):
    if x % i == 0:
      d.add(i)
      d.add(x // i)
  return sorted(d)


for x in range(500_000, 500_100):
  d = [i for i in div(x) if str(i)[-1] == '8' and str(i) != '8']
  if len(d) > 0:
    print(x, d[0])