from math import *
f = open('27A.txt')
n = open('27B.txt')

clusterA = [[], []]
clusterB = [[], [], []]

for s in f:
  s = s.replace(',', '.')
  x, y, b = [float(c) for c in s.split()]
  if x > 0:
    clusterA[0].append([x, y, b])
  else:
    clusterA[1].append([x, y, b])

for s in n:
  s = s.replace(',', '.')
  x, y, b = [float(c) for c in s.split()]
  if y < -2:
    clusterB[0].append([x, y, b])
  elif x > 0:
    clusterB[1].append([x, y, b])
  else:
    clusterB[2].append([x, y, b])

def center(cluster):
  best_center = [[] for _ in range(len(cluster))]
  for i in range(len(cluster)):
    min_sum_distance = 10 ** 10
    for x1, y1, b in cluster[i]:
      sum_distance = 0
      for x2, y2, b in cluster[i]:
        sum_distance += dist([x1, y1], [x2, y2])
      if sum_distance < min_sum_distance:
        min_sum_distance = sum_distance
        best_center[i] = [x1, y1, b]
  return best_center

center_clusterA = center(clusterA)
center_clusterB = center(clusterB)

def Harmonica(cluster):
  return len(cluster) / sum([1 / b for x, y, b in cluster])

H_A = []
H_B = []

for i in range(len(clusterA)):
  H_A.append(Harmonica(clusterA[i]))

for i in range(len(clusterB)):
  H_B.append(Harmonica(clusterB[i]))

P_xy_A = int(sum([x + y for x, y, b in center_clusterA]) * 10000)
P_h_A = int(sum(H_A) * 10000)

P_xy_B = int(sum([x + y for x, y, b in center_clusterB]) * 10000)
P_h_B = int(sum(H_B) * 10000)

print(P_xy_A, P_h_A)
print(P_xy_B, P_h_B)




































