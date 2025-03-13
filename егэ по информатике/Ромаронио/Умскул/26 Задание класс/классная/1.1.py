f = open('test.txt')
n, m, k = map(int, f.readline().split())
info_place = [m] * (k + 1)
for s in f:
  ryad, mesto = map(int, s.split())
  info_place[mesto] = min(info_place[mesto], ryad - 1)
  










