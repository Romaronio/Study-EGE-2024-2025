# from turtle import *
# k = 30
# screensize(-5000, 5000)
# tracer(0)
# pu()
# left(90)
# f = open('27A_19747.txt')
# for s in f:
#   x, y = s.split()
#   x, y = float(x), float(y)
#   goto(x * k, y * k)
#   dot(3)
# for x in range(-40, 40):
#   for y in range(-40, 40):
#     if x == 0 and y == 0:
#       dot(4,'blue')
#     else:
#       goto(x * k, y * k)
#       dot(3, 'red')
# done()

# from turtle import *
# k = 30
# screensize(-5000, 10000)
# tracer(0)
# pu()
# left(90)
# f = open('27B_19747.txt')
# for s in f:
#   x, y = s.split()
#   x, y = float(x), float(y)
#   goto(x * k, y * k)
#   dot(3)
# for x in range(-40, 40):
#   for y in range(-40, 40):
#     if x == 10 and y == 11 or x == 0 and y == 0:
#       dot(4,'red')
#     else:
#       goto(x * k, y * k)
#       dot(3, 'blue')
# done()

f = open('27A_19747.txt')
h = open('27B_19747.txt')
clusterA = [[], [], []]
clusterB = [[], [], [], [], []]

for s in f:
  x, y = s.split()
  x, y = float(x), float(y)
  if y < 6:
    clusterA[0].append([x, y])
  elif x > 5 and y > 6:
    clusterA[1].append([x, y])
  else:
    clusterA[2].append([x, y])

for s in h:
  x, y = s.split()
  x, y = float(x), float(y)
  if y < 11 and y > x + 1:
    clusterB[0].append([x, y])
  elif x < 10 and y < 11:
    clusterB[1].append([x, y])
  elif x > 10 and y < 11:
    clusterB[2].append([x, y])
  elif x > 9 and y > x + 1:
    clusterB[3].append([x, y])
  else:
    clusterB[4].append([x, y])

def centroid(cluster):
  best_centroid = [[] for i in range(len(cluster))]
  for i in range(len(cluster)):
    min_sum_dist = 10 ** 10
    for x1, y1 in cluster[i]:
      dists = 0
      for x2, y2 in cluster[i]:
        dists += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 1/2
      if dists < min_sum_dist:
        min_sum_dist = dists
        best_centroid[i] = [x1, y1]
  return best_centroid

centroidA = centroid(clusterA)
centroidB = centroid(clusterB)

P_x_A = int(((centroidA[0][0] + centroidA[1][0] + centroidA[2][0]) / 3) * 10000)
P_y_A = int(((centroidA[0][1] + centroidA[1][1] + centroidA[2][1]) / 3) * 10000)

P_x_B = int(((centroidB[0][0] + centroidB[1][0] + centroidB[2][0] + centroidB[3][0] + centroidB[4][0]) / 5) * 10000)
P_y_B = int(((centroidB[0][1] + centroidB[1][1] + centroidB[2][1] + centroidB[3][1] + centroidB[4][1]) / 5) * 10000)

print(P_x_A, P_y_A)
print(P_x_B, P_y_B)






