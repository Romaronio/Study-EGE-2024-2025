mas = []
for n in range(101, 1000):
  s = '1' * n
  while '111' in s:
    s = s.replace('111', '2', 1)
    s = s.replace('2222', '333',1)
    s = s.replace('33','1',1)
  mas.append([s, n, s.count('1')])
for i in mas:
  print(i)




