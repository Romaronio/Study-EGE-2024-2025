from math import *
f = open('27A.txt')
point = []
for s in f:
  s = s.replace(',','.')
  x, y = [float(c) for c in s.split()]
  point.append([x, y])
# k = 50
# screensize(5000, 5000)
# tracer(0)
# pu()
# for x, y in point:
#   goto(x * k, y * k)
#   dot()
# for x in range(-40, 40):
#   for y in range(-40, 40):
#     goto(x * k,y * k)
#     if x == 0 or y == 0:
#       dot(5, 'red')
#     else:
#       dot(3)
# setpos(0, 0)
# dot(10)
# done()

k_clusters = 2
clusters = [[] for _ in range(k_clusters)]
for x, y in point:
  if y > -4:
    clusters[0].append([x, y])
  else:
    clusters[1].append([x, y])
best_centroid = [[] for _ in range(k_clusters)]
for i in range(k_clusters):
  min_sum_dist = 10**10
  for x1, y1 in clusters[i]:
    sum_dict = 0
    for x2, y2 in clusters[i]:
      sum_dict += dist([x1, y1], [x2, y2])
    if sum_dict < min_sum_dist:
      min_sum_dist = sum_dict
      best_centroid[i] = [x1, y1]
P_x = int((sum([x for x, y in best_centroid]) / k_clusters) * 10000)
P_y = int((sum([y for x, y in best_centroid]) / k_clusters) * 10000)
print(P_x, P_y)
