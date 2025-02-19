f = open('9.txt')
k = 0
for s in f:
  a = list(map(int, s.split()))
  a.sort(reverse=True)
  if a[0] ** 2 == a[1] ** 2 + a[2] ** 2:
    k += 1
print(k)