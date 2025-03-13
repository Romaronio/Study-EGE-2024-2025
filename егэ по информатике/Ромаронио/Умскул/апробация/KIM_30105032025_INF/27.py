from math import *
f_b= open('301_27_B.txt')
f_a = open('301_27_A.txt')
k = 2

cluster_A = [[], []]
cluster_B = [[], [], []]

for s in f_b:
  s = s.replace(',', '.')
  x, y = [float(c) for c in s.split(' ')]
  if y < -5:
    cluster_B[0].append([x,y])
  if -5 < y < 5:
    cluster_B[1].append([x,y])
  else:
    cluster_B[2].append([x,y])

for s in f_a:
  s = s.replace(',', '.')
  x, y = [float(c) for c in s.split(' ')]
  if y < 1:
    cluster_A[0].append([x,y])
  else:
    cluster_A[1].append([x,y])

def centroid(cluster):
  best_centroid = [[] for i in range(len(cluster))]
  for i in range(len(cluster)):
    min_centroid = 10 ** 10
    for x1, y1 in cluster[i]:
      sum_dist = 0
      for x2, y2 in cluster[i]:
        sum_dist += dist([x1, y1], [x2, y2])
      if sum_dist <= min_centroid:
        min_centroid = sum_dist
        best_centroid[i] = [x1, y1]
  return best_centroid


centroid_A = centroid(cluster_A)
centroid_B = centroid(cluster_B)

P_x_A = int(sum([x for x, y in centroid_A]) * 10000)
P_y_A = int(sum([y for x, y in centroid_A]) * 10000)

P_x_B = int(sum([x for x, y in centroid_B]) * 10000)
P_y_B = int(sum([y for x, y in centroid_B]) * 10000)

print(P_x_A, P_y_A)
print(P_x_B, P_y_B)
