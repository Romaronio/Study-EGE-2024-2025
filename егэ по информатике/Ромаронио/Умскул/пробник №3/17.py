f = open('17_7020.txt')
a = []
for s in f:
  a.append(int(s))
for i in range(len(a) + 3):
  if min(a[i], a[i + 1], a[i + 2], a[i + 3]):
    print(len(a))