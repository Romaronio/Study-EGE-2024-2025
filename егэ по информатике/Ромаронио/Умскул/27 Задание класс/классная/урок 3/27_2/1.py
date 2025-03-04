# from turtle import *
# k = 30
# screensize(5000, 5000)
# pu()
# tracer(0)
# colors = ['green', 'blue', 'red', 'yellow', 'pink', 'black']
# for i in range(len(cluster)):
#   for x, y in cluster[i]:
#     setpos(x * k, y * k)
#     dot(5, colors[i])
# done()

from math import *
f = open('27B.txt')
f.readline()
points = [list(map(float, s.replace(',', '.').split())) for s in f]
def DBcsan(points):
  cluster,epsilon = [],0.5
  while points:
    cluster.append([points[0]])
    del points[0]
    for p1 in cluster[-1]:
      for p2 in points[:]:
        if dist(p1, p2) < epsilon:
          cluster[-1].append(p2)
          points.remove(p2)
    if len(cluster[-1]) <= 10:
      del cluster[-1]
  return cluster

def center(cluster):
  best_centroid = [[] for _ in range(len(cluster))]
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


cluster = DBcsan(points)

mas_centroid = center(cluster)


P_x = sum([x for x, y in mas_centroid]) / len(cluster)
P_y = sum([y for x, y in mas_centroid]) / len(cluster)
P_x_y = int((P_y + P_x) * 10000)
P_s = int(sum([len(cl) / 9 for cl in cluster]) * 1000)

print(P_x_y, P_s)

































