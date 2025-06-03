f = open('2.3.txt')
s = int(f.readline())
mas = []
block = []
for s in f:
  wight, color = s.split()
  mas.append([int(wight), color])

mas.sort(reverse=True)
while mas:
  res = [mas[0]]
  del mas[0]
  for i in mas[:]:
    if res[-1][0] - i[0] >= 8 and i[1] != res[-1][1]:
      res.append(i)
      mas.remove(i)
  block.append(res)

print(len(block), len(max(block)))



