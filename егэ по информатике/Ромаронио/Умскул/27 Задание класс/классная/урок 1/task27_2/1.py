from math import *
f = open('27A.txt')
n = open('27B.txt')
clusterA = [[], []]
clusterB = [[], [], []]
for s in f:
  s = s.replace(',', '.')
  x, y = [float(c) for c in s.split()]
  if x < 0:
    clusterA[0].append([x, y])
  else:
    clusterA[1].append([x, y])


for s in n:
  s = s.replace(',','.')
  x, y = [float(c) for c in s.split()]
  if x < -4:
    clusterB[0].append([x, y])
  elif y > 2:
    clusterB[1].append([x, y])
  else:
    clusterB[2].append([x, y])

def center(clusters):
  best_centroid = [[] for _ in range(len(clusters))]
  for i in range(len(clusters)):
    min_distance = 10 ** 10
    for x1, y1 in clusters[i]:
      current_distance = 0
      for x2, y2 in clusters[i]:
        current_distance += dist([x1, y1], [x2, y2])
      if current_distance < min_distance:
        min_distance = current_distance
        best_centroid[i] = [x1, y1]
  return best_centroid

center_clustersA = center(clusterA)
center_clustersB = center(clusterB)
P_x_A = int((sum(x for x, y in center_clustersA) / len(clusterA)) * 10000)
P_y_A = int((sum(y for x, y in center_clustersA) / len(clusterA)) * 10000)
P_x_B = int((sum(x for x, y in center_clustersB) / len(clusterB)) * 10000)
P_y_B = int((sum(y for x, y in center_clustersB) / len(clusterB)) * 10000)
print(P_x_A, P_y_A, P_x_B, P_y_B)

























