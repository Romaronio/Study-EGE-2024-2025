from math import *
f = open('27A.txt')
n = open('27B.txt')
clustersA = [[], []]
clustersB = [[], [], []]
for s in f:
  s = s.replace(',', '.')
  x, y = [float(c) for c in s.split()]
  if y > 0:
    clustersA[0].append([x, y])
  else:
    clustersA[1].append([x, y])

for s in n:
  s = s.replace(',', '.')
  x, y = [float(c) for c in s.split()]
  if y > 0:
    clustersB[0].append([x, y])
  elif x > -1:
    clustersB[1].append([x, y])
  else:
    clustersB[2].append([x, y])

def center(clusters):
  best_clusters_center = [[] for _ in range(len(clusters))]
  for i in range(len(clusters)):
    min_clusters_distance = 10**10
    for x1, y1 in clusters[i]:
      current_distance = 0
      for x2, y2 in clusters[i]:
        current_distance += dist([x1, y1], [x2, y2])
      if current_distance < min_clusters_distance:
        min_clusters_distance = current_distance
        best_clusters_center[i] = [x1, y1]
  return best_clusters_center


center_clustersA = center(clustersA)
center_clustersB = center(clustersB)

P_x_A = int((sum(x for x, y in center_clustersA) / len(clustersA) * 10000))
P_y_A = int((sum(y for x, y in center_clustersA) / len(clustersA) * 10000))
P_x_B = int((sum(x for x, y in center_clustersB) / len(clustersB) * 10000))
P_y_B = int((sum(y for x, y in center_clustersB) / len(clustersB) * 10000))
print(P_x_A, P_y_A)
print(P_x_B, P_y_B)

