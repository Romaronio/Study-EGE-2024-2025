def Del(s):
  mas = set()
  for i in range(2, int(s ** 0.5) + 1):
    if s % i == 0:
      mas.add(i)
      mas.add(s // i)
  mas = sorted(mas)
  if mas:
    return max(mas) - min(mas)
  else:
    return None

for s in range(700_000, 700_500):
  res = Del(s)
  if res is not None and res % 54 == 17:
    print(s, res)
