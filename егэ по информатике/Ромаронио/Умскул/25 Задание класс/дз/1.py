def div(x):
  d = set()
  for i in range(2, int(x ** 0.5) + 1):
    if x % i == 0:
      d.add(i)
      d.add(x // i)
  return sorted(d)

for x in range(174457, 174506):
  if len(div(x)) == 2:
    print(*div(x))