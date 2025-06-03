f = open('17.txt')
m = f.readlines()
mas = []
mas2 = []
for i in range(len(m) - 2):
    mas.append([int(m[i]), int(m[i + 1]), int(m[i + 2])])

for i in mas:
    if max(i) * min(i) > sum([x for x in i if x > 0]):
        mas2.append(sum(i))

print(len(mas2), min(mas2))
