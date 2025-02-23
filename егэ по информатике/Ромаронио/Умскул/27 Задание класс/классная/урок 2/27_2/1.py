from math import *
f = open('27A.txt')
n = open('27B.txt')

clustersA = [[], []]
clustersB = [[], [], []]

for s in f:
  s = s.replace(',', '.')
  x, y, b = [float(c) for c in s.split()]
  if y < 2:
    clustersA[0].append([x, y, b])
  else:
    clustersA[1].append([x, y, b])

for s in n:
  s = s.replace(',', '.')
  x, y, b = [float(c) for c in s.split()]
  if x < -2:
    clustersB[0].append([x, y, b])
  elif y > -1:
    clustersB[1].append([x,y, b])
  else:
    clustersB[2].append([x, y, b])

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

center_clusterA = center(clustersA)
center_clusterB = center(clustersB)

def mediana(cluster):
  Sorted_b = sorted([b for x, y, b in cluster])
  n = len(Sorted_b)
  if n % 2 == 1:
    return Sorted_b[n // 2]
  else:
    return (Sorted_b[n // 2] + Sorted_b[(n // 2) - 1]) / 2

M_A = int(sum([mediana(clustersA[i]) for i in range(len(clustersA))]) * 10000)
M_B = int(sum([mediana(clustersB[i]) for i in range(len(clustersB))]) * 10000)



Sum_x_y_A = int(sum([x + y for x, y, b in center_clusterA]) * 10000)
Sum_x_y_B = int(sum([x + y for x, y, b in center_clusterB]) * 10000)

print(Sum_x_y_A, M_A)
print(Sum_x_y_B, M_B)






























