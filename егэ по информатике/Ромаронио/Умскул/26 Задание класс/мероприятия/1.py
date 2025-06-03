f = open('1.txt')
s = int(f.readline())
data = []
for s in f:
  start, end = map(int, s.split())
  data.append([end, start])

data.sort()
zal = 0
podoshel = []
for end, start in data:
  if start >= zal:
    zal = end
    podoshel.append([start, end])
  if start >= 1379:
    print(start, end)

print(len(podoshel))