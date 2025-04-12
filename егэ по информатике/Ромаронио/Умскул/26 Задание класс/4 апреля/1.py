f = open('26.1.txt')
n = int(f.readline())
day = [0]*1440
for s in f:
  start, end = map(int, s.split())
  for t in range(start, end):
    day[t] += 1

print(max(day))
print([t for t in range(1440) if day[t] == 5062])
