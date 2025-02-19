def three(n):
  s = ''
  while n > 0:
    s += str(n % 3)
    n = n // 3
  return s
res_mas = []
for k in range(101):
  k = three(k)
  k = str(k)
  k += str(three(k.count('2')))
  k += str(three(k.count('1')))
  if k.count('0') == 0:
    k += str('0')
  else:
    k += str(three(k.count('0')))
  if int(k, 3) <= 1000:
    res_mas.append(int(k, 3))
print(max(res_mas))