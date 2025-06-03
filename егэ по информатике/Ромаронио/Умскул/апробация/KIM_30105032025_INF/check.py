import math
from turtle import *
from math import dist
def visual(clusters):
    k = 40
    penup(), tracer(0)
    colors = ['green', 'blue', 'brown', 'red', 'yellow', 'pink', 'black']
    for i in range(len(clusters)):
        for x, y in clusters[i]:
            setpos(x*k, y*k)
            dot(5, colors[i])
    done()

def centroid(cluster):
    c = []
    for x1, y1 in cluster:
        c += [[sum(math.dist((x1, y1), (x2, y2)) for x2, y2 in cluster), (x1, y1)]]
    return min(c)[1]

f = open('301_27A.txt')
f.readline()
points = [list(map(float, s.replace(",", ".").split())) for s in f]
clusters, epsilon = [], 1
while points:
    clusters.append([points[0]])
    del points[0]
    for p1 in clusters[-1]:
        for p2 in points[:]:
            if math.dist(p1, p2) < epsilon:
                clusters[-1].append(p2)
                points.remove(p2)
visual(clusters)
Px = sum([centroid(clusters[i])[0] for i in range(len(clusters))]) / len(clusters)
Py = sum([centroid(clusters[i])[1] for i in range(len(clusters))]) / len(clusters)
print(int(Px * 10000), int(Py * 10000))