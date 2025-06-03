f = open('27A.txt')
h = open('27B.txt')

ClusterA = [[], []]
ClusterB = [[], [], [], []]

for s in f:
  x, y = map(float, s.split())
  if x > 2:
    ClusterA[0].append([x, y])
  if x < 2:
    ClusterA[1].append([x, y])


for s in h:
  x,y = map(float, s.split())
  if x < -6:
    ClusterB[0].append([x, y])
  elif x > -6 and y < -6:
    ClusterB[1].append([x,y])
  elif x > -6 and y > -6 and y < -2.5:
    ClusterB[2].append([x, y])
  else:
    ClusterB[3].append([x, y])

def centroid(cluster):
  best_centroid = [i for i in range(len(cluster))]
  for i in range(len(cluster)):
    min_sum = 10 ** 10
    for x1, y1 in cluster[i]:
      sum_dist = 0
      for x2, y2 in cluster[i]:
        sum_dist += (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
      if sum_dist < min_sum:
        min_sum = sum_dist
        best_centroid[i] = [x1, y1]
  return best_centroid


center_clusterA = centroid(ClusterA)
center_clusterB = centroid(ClusterB)

P_x_A = int((sum(x for x, y in center_clusterA) / len(ClusterA)) * 10000)
P_y_A = int((sum(y for x, y in center_clusterA) / len(ClusterA)) * 10000)
P_x_B = int((sum(x for x, y in center_clusterB) / len(ClusterB)) * 10000)
P_y_B = int((sum(y for x, y in center_clusterB) / len(ClusterB)) * 10000)

# P_x_A = int(((centroidA[0][0] + centroidA[1][0]) / 2) * 10000)
# P_y_A = int(((centroidA[0][1] + centroidA[1][1]) / 2) * 10000)
#
# P_x_B = int(((centroidB[0][0] + centroidB[1][0] + centroidB[2][0] + centroidB[3][0]) / 4) * 10000)
# P_y_B = int(((centroidB[0][1] + centroidB[1][1] + centroidB[2][1] + centroidB[3][1]) / 4) * 10000)

print(P_x_A, P_y_A)
print(P_x_B, P_y_B)