f = open('27A.txt')

k = 2
clusterA = [[] for _ in range(k)]
for s in f:
  s = s.replace(',','.')
  x, y = [float(c) for c in s.split()]
  if y < -4:
    clusterA[0].append([x, y])
  elif y > 4:
    clusterA[1].append([x, y])

def dist(p1, p2):
  x1, y1, x2, y2 = *p1, *p2
  return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def center(kl):
  m = []
  for p in kl:
    sm = sum(dist(p, p1) for p1 in kl)
    m.append([sm, p])
    print(m)
  return min(m)

centerA = [center(a) for a in clusterA]

print(centerA)
