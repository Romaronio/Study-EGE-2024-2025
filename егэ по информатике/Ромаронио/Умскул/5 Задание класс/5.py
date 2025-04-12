a = []
for n in range(1, 10000):
  s = bin(n)[2:]
  if n % 2 == 0:
    s += s[:2]
  else:
    s = '1' + s + '0'
  if int(s, 2) > 410:
    a.append(int(s, 2))
print(min(a))