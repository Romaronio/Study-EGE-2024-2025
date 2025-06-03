f = open('27.1.A.txt')
h = open('27.1.В.txt')

ClusterA = [[], []]
ClusterB = [[], [], []]

for s in f:
    x, y = map(float, s.split())
    if x < 1:
        ClusterA[0].append([x, y])
    else:
        ClusterA[1].append([x, y])

for s in h:
    x, y = map(float, s.split())
    if x < 0 and y < 0:
        ClusterB[0].append([x, y])
    if x < 0 and y > 0:
        ClusterB[1].append([x, y])
    if x > 0:
        ClusterB[2].append([x, y])

def centroid(cluster):
    best_centroid = [[] for i in range(len(cluster))]
    for i in range(len(cluster)):
        min_dist = 10 ** 10
        for x1, y1 in cluster[i]:
            dist = 0
            for x2, y2 in cluster[i]:
                dist += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if min_dist > dist:
                min_dist = dist
                best_centroid[i] = [x1, y1]
    return best_centroid

centroid_ClusterA = centroid(ClusterA)
centroid_ClusterB = centroid(ClusterB)

P_x_A = int((sum([i[0] for i in centroid_ClusterA]) / len(centroid_ClusterA)) * 10000)
P_y_A = int((sum([i[1] for i in centroid_ClusterA]) / len(centroid_ClusterA)) * 10000)

P_x_B = int((sum([i[0] for i in centroid_ClusterB]) / len(centroid_ClusterB)) * 10000)
P_y_B = int((sum([i[1] for i in centroid_ClusterB]) / len(centroid_ClusterB)) * 10000)

print(P_x_A, P_y_A)
print(P_x_B, P_y_B)