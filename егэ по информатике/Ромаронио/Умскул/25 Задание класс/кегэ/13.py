def simple(x):
  return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

def div(x):
  d = set()
  for i in range(1, int(x ** 0.5) + 1):
    if x % i == 0:
      d.add(i)
      d.add(x // i)
  return sorted(d)

for x in range(650_001, 650_900):
  d = [i for i in div(x) if simple(i)]
  if sum(d) % 100 == 25:
    print(x, sum(d))