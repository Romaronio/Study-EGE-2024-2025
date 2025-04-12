clustersA = [[], []]
clustersB = [[], [], []]

for s in open('27A_1.txt'):
  x, y = [float(c) for c in s.split()]
  if y > 2:
    clustersA[0].append([x, y])
  else:
    clustersA[1].append([x, y])

for s in open('27B_1.txt'):
  x, y = [float(c) for c in s.split()]
  if x < 2:
    clustersB[0].append([x, y])
  if x > 2 and y > 0:
    clustersB[1].append([x, y])
  if y < 0:
    clustersB[2].append([x, y])

def dist(A, B):
  x1, y1, x2, y2 = *A, *B
  return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def centroid(clusters):
  res = []
  for x1, y1 in clusters:
    sm = []
    for x2, y2 in clusters:
      sm.append(dist([x1, y1], [x2, y2]))
    res.append([sum(sm), [x1, y1]])
  return min(res)

CentroidA0 = centroid(clustersA[0])
CentroidA1 = centroid(clustersA[1])

CentroidB0 = centroid(clustersB[0])
CentroidB1 = centroid(clustersB[1])
CentroidB2 = centroid(clustersB[2])

print(CentroidA0[1][0])

P_x_A = int(((CentroidA0[1][0] + CentroidA1[1][0]) / 2) * 10000)
P_y_A = int(((CentroidA0[1][1] + CentroidA1[1][1]) / 2) * 10000)

P_x_B = int(((CentroidB0[1][0] + CentroidB1[1][0] + CentroidB2[1][0]) / 3) * 10000)
P_y_B = int(((CentroidB0[1][1] + CentroidB1[1][1] + CentroidB2[1][1]) / 3) * 10000)


print(P_x_A, P_y_A, P_x_B, P_y_B)




