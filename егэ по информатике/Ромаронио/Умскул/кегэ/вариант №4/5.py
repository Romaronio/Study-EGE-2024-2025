k = 0
for n in range(1, 1000):
  s = hex(n)[2:]
  if s.count('b') % 2 == 0:
    s = '1' + s
  else:
    s = s + '1'
  if len(str(int(s, 16))) == 2:
    k += 1
    print(s)

print(k)