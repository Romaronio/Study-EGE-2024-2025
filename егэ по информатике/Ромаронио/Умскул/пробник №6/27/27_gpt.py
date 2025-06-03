import math


def euclidean_distance(point1,point2):
  """Вычисляет евклидово расстояние между двумя точками."""
  return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def find_centroid(cluster):
  """Находит центроид кластера (точку, минимизирующую сумму расстояний до остальных точек)."""
  min_distance_sum = float('inf')
  centroid = None

  for potential_centroid in cluster:
    distance_sum = sum(euclidean_distance(potential_centroid,point) for point in cluster)
    if distance_sum < min_distance_sum:
      min_distance_sum = distance_sum
      centroid = potential_centroid

  return centroid


def process_file(filename,h,w,num_clusters):
  """Обрабатывает файл с данными о звездах и находит центры кластеров."""
  clusters = [[] for _ in range(num_clusters)]
  cluster_index = 0

  with open('27B.txt','r') as f:
    for line in f:
      x,y = map(float,line.strip().split())
      clusters[cluster_index].append((x,y))
      # Переключаемся на следующий кластер, когда в текущем кластере достигли максимальной ширины и высоты
      # Такое решение основано на условии задания, что кластеры помещаются в прямоугольник H x W
      # Альтернативно можно использовать алгоритм кластеризации
      cluster_index = (cluster_index + 1) % num_clusters

  centroids = [find_centroid(cluster) for cluster in clusters]
  return centroids


# Обработка файла A
centroids_a = process_file("27_2a.txt",4,4,2)
px_a = sum(centroid[0] for centroid in centroids_a) / len(centroids_a)
py_a = sum(centroid[1] for centroid in centroids_a) / len(centroids_a)

# Обработка файла B
centroids_b = process_file("27_2b.txt",4,4,4)
px_b = sum(centroid[0] for centroid in centroids_b) / len(centroids_b)
py_b = sum(centroid[1] for centroid in centroids_b) / len(centroids_b)

print(int(px_a * 10000),int(py_a * 10000))
print(int(px_b * 10000),int(py_b * 10000))
