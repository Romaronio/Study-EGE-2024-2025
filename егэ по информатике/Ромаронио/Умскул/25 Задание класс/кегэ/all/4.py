def div(x):
  dives = set()
  for i in range(1, int(x ** 0.5) + 1):
    if x % i == 0:
      dives.add(i)
      dives.add(x // i)
  return sorted(dives)

for x in range(244143, 367822):
  if int(x ** 0.5) ** 2 == x:
    d = div(x)
    if len(d) == 5:
      print(d[3], d[4])