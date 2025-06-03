def div(x):
  d = set()
  for i in range(1, int(x**1/2) + 1):
    if x % i == 0:
      d.add(i)
      d.add(x // i)
  return sorted(d)

for x in range(193136, 193224):
  if len(div(x)) == 6:
    print(div(x))