def div(x):
  d = set()
  for i in range(1, int(x ** 0.5) + 1):
    if x % i == 0:
      d.add(i)
      d.add(x // i)
  return sorted(d)

def simple(x):
  return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) +1))

mas = []
for x in range(158928, 345293 + 1):
  d = [i for i in div(x) if simple(i)]
  if len(d) == 3:
    if d[0] * d[1] * d[2] == x:
      mas.append(x)

print(len(mas), min(mas))