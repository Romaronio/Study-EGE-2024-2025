f = open('27A.txt')
h = open('27B.txt')
ClusterA = [[], [], []]
ClusterB = [[], [], [], [], []]

for s in f:
    x, y = map(float, s.split())
    if x < -2 and y > 0:
        ClusterA[0].append([x, y])
    if x > -2 and y > -2:
        ClusterA[1].append([x, y])
    if y < -2:
        ClusterA[2].append([x, y])

for s in h:
    x, y = map(float, s.split())
    if y > 3:
        ClusterB[0].append([x, y])
    if y < 2 and x < -3:
        ClusterB[1].append([x, y])
    if y < 1 and x < 1 and x > -3:
        ClusterB[2].append([x, y])
    if x > 1 and y > -2.2:
        ClusterB[3].append([x, y])
    if x > 1 and y < -2.2:
        ClusterB[4].append([x, y])


def centroid(cluster):
    best_centtoid = [i for i in range(len(cluster))]
    for i in range(len(cluster)):
        min_sum_dist = 10 ** 10
        for x1, y1 in cluster[i]:
            dist = 0
            for x2, y2 in cluster[i]:
                dist += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if min_sum_dist > dist:
                min_sum_dist = dist
                best_centtoid[i] = [x1, y1]
    return best_centtoid

centroid_ClusterA = centroid(ClusterA)
centroid_ClusterB = centroid(ClusterB)

P_x_A = int(sum([x for x, y in centroid_ClusterA]) / len(centroid_ClusterA) * 10000)
P_y_A = int(sum([y for x, y in centroid_ClusterA]) / len(centroid_ClusterA) * 10000)

P_x_B = int(sum([x for x, y in centroid_ClusterB]) / len(centroid_ClusterB) * 10000)
P_y_B = int(sum([y for x, y in centroid_ClusterB]) / len(centroid_ClusterB) * 10000)

print(P_x_A, P_y_A)
print(P_x_B, P_y_B)