from math import sqrt

f = open('27_A_17915.txt')
h = open('27_B_17915.txt')
clusterA = [[], [], []]
clusterB = [[], [], [], []]
for s in f:
  x, y = [float(c) for c in s.split()]
  if x < 6:
    clusterA[0].append([x, y])
  elif y > 23 and x > 6:
    clusterA[1].append([x, y])
  else:
    clusterA[2].append([x, y])

for s in h:
  x, y = [float(c) for c in s.split()]
  if y > 14 and x < 15:
    clusterB[0].append([x, y])
  elif y < 12 and x < 15:
    clusterB[1].append([x, y])
  elif x > 15 and y < 12:
    clusterB[2].append([x, y])
  else:
    clusterB[3].append([x, y])

def math_dist(x1, y1, x2, y2):
  return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

def centroid(cluster):
  best_centroid = [[] for i in range(len(cluster))]
  for i in range(len(cluster)):
    min_sum_dist = 10**10
    for x1, y1 in cluster[i]:
      dists = 0
      for x2, y2 in cluster[i]:
        dists += math_dist(x1, y1, x2, y2)
      if min_sum_dist > dists:
        min_sum_dist = dists
        best_centroid[i] = [x1, y1]
  return best_centroid


centerA = centroid(clusterA)
centerB = centroid(clusterB)

print(centerA, centerB)

P_x_A = int((sum(x for x, y in centerA) / len(clusterA)) * 10000)
P_y_A = int((sum(y for x, y in centerA) / len(clusterA)) * 10000)
P_x_B = int((sum(x for x, y in centerB) / len(clusterB)) * 10000)
P_y_B = int((sum(y for x, y in centerB) / len(clusterB)) * 10000)

print(P_x_A, P_y_A)
print(P_x_B, P_y_B)
























