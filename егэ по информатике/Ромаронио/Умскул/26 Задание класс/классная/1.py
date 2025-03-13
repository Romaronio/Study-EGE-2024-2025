f = open('task1.txt')
n, m, k = map(int, f.readline().split())
info_place = [m] * (k + 1)
for s in f:
  ryad, mesto = map(int, s.split())
  info_place[mesto] = min(info_place[mesto], ryad - 1)
res = []
for i in range(1, len(info_place) - 1):
  left, right = info_place[i], info_place[i + 1]
  res.append([min(left, right), i, i+1])
print(max(res))