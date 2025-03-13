f = open('task1.txt')
n, m, k = map(int, f.readline().split())
info_place = [m] * (k + 1)
for s in f:
  ryad, mesto = map(int, s.split())
  info_place[mesto] = min(info_place[mesto], ryad - 1)
res = []
for i in range(1, k):
  left, right = info_place[i], info_place[i + 1]
  res.append([i, i + 1, min(left, right)])
print(max(res))