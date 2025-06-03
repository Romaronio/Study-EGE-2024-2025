f = open('26.1.txt')
k = int(f.readline())
n = int(f.readline())
files = []
cnt, last_disk = 0, 0
for s in f:
  start, end = map(int, s.split())
  files.append([start, end])

files.sort()

disks = [0] * k

for start, end in files:
  for i in range(k):
    if start > disks[i]:
      disks[i] = end
      cnt += 1
      last_disk = (i + 1)
      break

print(cnt, last_disk)
