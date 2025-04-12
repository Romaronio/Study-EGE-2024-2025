f = open('17.txt')
mas = []
for s in f:
  s = s.replace('\n', '')
  mas.append(int(s))

k = 0
mas.sort()
for i in range(len(mas) - 1):
  if mas[i] % 16 == mas[0] or mas[i + 1] % 16 == mas[0]:
    k += 1

print(k)