f = open('26.2.2.txt')
s = int(f.readline())
mas = [int(i) for i in f]
mas.sort()
block = []
res = []
while mas:
  if len(res) == 0:
    res = [mas[0]]
    del mas[0]
  for i in mas[:]:
    if i - 5 > res[-1]:
      res.append(i)
      mas.remove(i)
  else:
    block.append(res)
    res = []
print(len(block), len(block[0]))