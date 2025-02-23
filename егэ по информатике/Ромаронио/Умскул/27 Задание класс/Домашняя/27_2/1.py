from math import *
f = open('27A.txt')
n = open('27B.txt')
clusterA = [[], []]
clusterB = [[], [], []]
for s in f:
  s = s.replace(',', '.')
  x, y = [float(c) for c in s.split()]
  if y > 1:
    clusterA[0].append([x, y])
  else:
    clusterA[1].append([x, y])

for s in n:
  s = s.replace(',', '.')
  x, y = [float(c) for c in s.split()]
  if y < -0.9:
    clusterB[0].append([x, y])
  elif x > 0:
    clusterB[1].append([x, y])
  else:
    clusterB[2].append([x, y])

def center(cluster):
  best_distance = [[] for _ in range(len(cluster))]
  for i in range(len(cluster)):
    min_sum_distance = 10 ** 10
    for x1, y1 in cluster[i]:
      sum_distance = 0
      for x2, y2 in cluster[i]:
        sum_distance += dist([x1, y1], [x2, y2])
      if sum_distance < min_sum_distance:
        min_sum_distance = sum_distance
        best_distance[i] = [x1, y1]
  return best_distance

center_clusterA = center(clusterA)
center_clusterB = center(clusterB)

P_x_A = int((sum(x for x, y in center_clusterA) / len(clusterA)) * 10000)
P_y_A = int((sum(y for x, y in center_clusterA) / len(clusterA)) * 10000)
P_x_B = int((sum(x for x, y in center_clusterB) / len(clusterB)) * 10000)
P_y_B = int((sum(y for x, y in center_clusterB) / len(clusterB)) * 10000)

print(P_x_A, P_y_A, P_x_B, P_y_B)










