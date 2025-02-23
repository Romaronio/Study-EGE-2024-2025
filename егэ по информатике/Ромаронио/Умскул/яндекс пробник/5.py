def three(n):
  res = ''
  alfavit = '0123456789ABCDEFGHIJKLMNO'
  while n > 0:
    res = alfavit[n % 3] + res
    n = n // 3
  return res
m = []
for n in range(1, 100):
  s = str(three(n))
  s = s + str(three(s.count('2')))
  s = s + str(three(s.count('1')))
  s = s + str(three(s.count('0')))
  if int(s, 3) < 1000:
    m.append(int(s, 3))
    print(max(m), n)