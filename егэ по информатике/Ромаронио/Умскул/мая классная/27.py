import math
f = open('27A.txt')
h = open('27B.txt')

clusterA = [[], []]
clusterB = [[], [], []]

for s in f:
  x, y = map(float, s.split())
  if y > 10:
    clusterA[1].append([x, y])
  else:
    clusterA[0].append([x, y])

for s in h:
  x, y = map(float, s.split())
  if y < 10:
    clusterB[0].append([x, y])
  elif y > 10 and x > 17:
    clusterB[1].append([x, y])
  else:
    clusterB[2].append([x, y])

def antucentroid(cluster):
  best_centroid = [i for i in range(len(cluster))]
  for i in range(len(cluster)):
    max_dist = 0
    for x1, y1 in cluster[i]:
      dist = 0
      for x2, y2 in cluster[i]:
        dist += math.dist([x1, y1], [x2, y2])
      if max_dist < dist:
        max_dist = dist
        best_centroid[i] = [len(cluster[i]), x1, y1]
  print(best_centroid)
  return best_centroid


nedocenterA = antucentroid(clusterA)
nedocenterB = antucentroid(clusterB)


P_x_A = nedocenterA[0][1]
P_y_A = nedocenterA[0][2]

P_x_B = nedocenterB[0][1]
P_y_B = nedocenterB[0][2]

print(P_x_A, P_y_A)
print(P_x_B, P_y_B)













