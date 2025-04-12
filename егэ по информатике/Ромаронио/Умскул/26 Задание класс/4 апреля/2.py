f = open('26.2.txt')
n = int(f.readline())
sec = [0] * 86400
for s in f:
  start, end = map(int, s.split())
  for t in range(start, end):
      sec[t] += 1

print(max(sec))
print(max(sec[8 * 60 * 60 : 14 * 60 * 60 + 1]))
print(sec[8 * 60 * 60 : 14 * 60 * 60 + 1].count(max(sec[8 * 60 * 60 : 14 * 60 * 60 + 1])))
