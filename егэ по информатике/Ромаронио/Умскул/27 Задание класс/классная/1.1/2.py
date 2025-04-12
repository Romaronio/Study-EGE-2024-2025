clusterA = [[], []]
clusterB = [[], [], []]

for s in open('27A_2.txt'):
  x, y = [float(c) for c in s.split()]
  if x < 0:
    clusterA[0].append([x, y])
  else:
    clusterA[1].append([x, y])

for m in open('27B_2.txt'):
  x, y = [float(c) for c in m.split()]
  if y < -1:
    clusterB[0].append([x, y])
  elif x < -3:
    clusterB[1].append([x, y])
  else:
    clusterB[2].append([x, y])

def dist(A, B):
  x1, y1, x2, y2 = *A, *B
  return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def centroid(cluster):
  res = []
  for x1, y1 in cluster:
    sm = 0
    for x2, y2 in cluster:
      sm += dist([x1, y1], [x2, y2])
    res.append([sm, [x1, y1]])
  return min(res)

centroidA0 = centroid(clusterA[0])
centroidA1 = centroid(clusterA[1])

centroidB0 = centroid(clusterB[0])
centroidB1 = centroid(clusterB[1])
centroidB2 = centroid(clusterB[2])


P_A_x = int(((centroidA0[1][0] + centroidA1[1][0]) / 2) * 10000)
P_A_y = int(((centroidA0[1][1] + centroidA1[1][1]) / 2) * 10000)

P_B_x = int(((centroidB0[1][0] + centroidB1[1][0] + centroidB2[1][0]) / 3) * 10000)
P_B_y = int(((centroidB0[1][1] + centroidB1[1][1] + centroidB2[1][1]) / 3) * 10000)

print(P_A_x, P_A_y)
print(P_B_x, P_B_y)














