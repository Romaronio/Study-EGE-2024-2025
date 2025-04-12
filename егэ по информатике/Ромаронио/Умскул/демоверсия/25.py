def Del(x):
  d = set()
  for i in range(2, int(x ** 1/2) + 1):
    if x % i == 0:
      d.add(i)
      d.add(x // i)
  return sorted(d)


for s in range(800_000, 800_100):
  if len(Del(s)) > 0:
    m = Del(s)[0] + Del(s)[-1]
  else:
    m = 0
  if str(m)[-1] == '4':
    print(s, m)