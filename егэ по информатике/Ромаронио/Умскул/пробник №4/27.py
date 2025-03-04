from math import *
f = open('27A.txt')
point = [list(map(float, s.replace(',', '.').split())) for s in f]


def Dbscan():
  cluster, epson = [], 0.8
  while point:
    cluster.append([point[0]])
    del point[0]
    for p1 in cluster[-1]:
      for p2 in point[:]:
        if dist(p1, p2) < epson:
          cluster[-1].append(p2)
          point.remove(p2)
  return cluster


def centroid(cluster):
  best_centroid = [[] for _ in cluster]
  for i in range(len(cluster)):
    min_sum_dist = 10**10
    for x1, y1 in cluster[i]:
      sum_dist = 0
      for x2, y2 in cluster[i]:
        sum_dist += dist([x1, y1], [x2, y2])
        if min_sum_dist > sum_dist:
          min_sum_dist = sum_dist
          best_centroid[i] = [x1, y1]
  return best_centroid


cluster = Dbscan()
centroid_cluster = centroid(cluster)

P_x = int((sum(x for x, y in centroid_cluster) / len(cluster)) * 10000)
P_y = int((sum(y for x, y in centroid_cluster) / len(cluster)) * 10000)

print(P_x, P_y)

