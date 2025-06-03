f = open('27A.txt')
h = open('27B.txt')

clusterA = [[], [], []]
clusterB = [[], [], [], []]

for s in f:
  x, y = map(float, s.split())
  if x < 2:
    clusterA[0].append([x, y])
  elif x > 2 and y < 2:
    clusterA[1].append([x, y])
  else:
    clusterA[2].append([x, y])

for s in h:
  x, y = map(float, s.split())
  if x < -4:
    clusterB[0].append([x, y])
  elif x > -4 and x < 2:
    clusterB[1].append([x, y])
  elif x > 2 and y > -2:
    clusterB[2].append([x, y])
  else:
    clusterB[3].append([x, y])


def centroid(cluster):
  best_centroid = [i for i in range(len(cluster))]
  for i in range(len(cluster)):
    min_sum_dist = 10**10
    for x1, y1 in cluster[i]:
      dist = 0
      for x2, y2 in cluster[i]:
        dist += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
      if min_sum_dist > dist:
        min_sum_dist = dist
        best_centroid[i] = [x1, y1]
  return best_centroid

centerA = centroid(clusterA)
centerB = centroid(clusterB)

P_x_A = int(((centerA[0][0] + centerA[1][0] + centerA[2][0]) / 3) * 10000)
P_y_A = int(((centerA[0][1] + centerA[1][1] + centerA[2][1]) / 3) * 10000)

P_x_B = int(((centerB[0][0] + centerB[1][0] + centerB[2][0] + centerB[3][0]) / 4) * 10000)
P_y_B = int(((centerB[0][1] + centerB[1][1] + centerB[2][1] + centerB[3][1]) / 4) * 10000)

print(P_x_A, P_y_A)
print(P_x_B, P_y_B)















