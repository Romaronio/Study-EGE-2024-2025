import math
f = open('27A.txt')
f.readline()
point = [list(map(float, s.replace(',', '.').split())) for s in f]
cluster, epsilon = [], 0.5
while point:
  cluster.append([point[0]])
  del point[0]
  for p1 in cluster[-1]:
    for p2 in point[:]:
      if math.dist(p1, p2) < epsilon:
        cluster[-1].append(p2)
        point.remove(p2)
# from turtle import *
# k = 100
# screensize(5000, 5000)
# pu()
# tracer(0)
# colors = ['green', 'blue', 'red', 'yellow', 'pink', 'black']
# for i in range(len(cluster)):
#   for x, y in cluster[i]:
#     setpos(x * k, y * k)
#     dot(5, colors[i])
# done()

def center(cluster):
  best_centroid = [[]for i in range(len(cluster))]
  for i in range(len(cluster)):
    min_sum_dist = 10**10
    for x1, y1 in cluster[i]:
      sum_dist = 0
      for x2, y2 in cluster[i]:
        sum_dist += math.dist([x1, y1], [x2, y2])
      if sum_dist < min_sum_dist:
        min_sum_dist = sum_dist
        best_centroid[i] = [x1, y1]
  return best_centroid

center_cluster = center(cluster)
P_x = int((sum([x for x, y in center_cluster]) / len(cluster)) * 10000)
P_y = int((sum([y for x, y in center_cluster]) / len(cluster)) * 10000)

print(P_x, P_y)
































