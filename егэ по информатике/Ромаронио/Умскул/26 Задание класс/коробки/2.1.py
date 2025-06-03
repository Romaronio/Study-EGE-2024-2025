f = open('2.1.txt')
mas = [int(i) for i in f]
mas.sort(reverse=True)
res = [mas[0]]
for i in mas[:]:
  if res[-1] >= i + 5:
    res.append(i)
    mas.remove(i)


print(len(res), min(res))







