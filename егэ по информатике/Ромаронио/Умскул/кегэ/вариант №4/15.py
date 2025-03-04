def Del(n, m):
  return n % m == 0

res = []
for a in range(1, 100):
  for x in range(1, 10000):
    if (not(Del(x, 84)) or (not(Del(x, 90)))) <= (not(Del(x, a))):
      break
    res.append(a)

print(res)