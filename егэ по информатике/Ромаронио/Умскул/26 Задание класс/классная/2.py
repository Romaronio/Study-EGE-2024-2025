f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\26 Задание класс\дз\task2.txt')
n, m, k = map(int, f.readline().split())
info_place = [[] for i in range(k + 1)]
res = []
for s in f:
  ryad, mesto = map(int, s.split())
  info_place[mesto].append(ryad)
for i in range(1, len(info_place)):
  info_place[i] = sorted([0] + info_place[i] + [m + 1], reverse=True)
  for J in range(len(info_place[i]) - 1):
    up, down = info_place[i][J], info_place[i][J + 1]
    res.append([up - down - 1 - 1, up - 1])
print(max(res))
