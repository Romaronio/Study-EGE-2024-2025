def Del(n, m):
  return n % m == 0

def f(x, a):
  return (Del(x, 34) and (not(Del(x, 51)))) <= ((not(Del(x, a))) or Del(x, 51))

mas = []
for a in range(1, 1000):
  for x in range(1, 10000):
    if f(x, a) == 0:
      break
  else:
    mas.append(a)

print(mas)