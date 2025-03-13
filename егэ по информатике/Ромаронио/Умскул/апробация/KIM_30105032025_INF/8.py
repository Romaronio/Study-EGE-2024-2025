k = 0
for s in range(10000, 99999 + 1):
  s = str(s)
  if s.count('0') == 1:
    s = s.replace('1', 'a')
    s = s.replace('3','a')
    s = s.replace('5','a')
    s = s.replace('7','a')
    s = s.replace('9','a')
    if 'aa' not in s:
      k += 1
print(k)