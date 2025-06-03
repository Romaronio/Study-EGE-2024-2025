f = open('26_6031.txt')
s = f.readline()
mas = [int(i) for i in f]
mas.sort()
res_mas = []
res_mas.append(int(mas[-1]))
mas.remove(mas[-1])
for i in sorted(mas, reverse=True):
    print(i)
    if int(i) <= res_mas[-1] - 6:
        res_mas.append(int(i))
    mas.remove(mas[-1])


print(len(res_mas), min(res_mas))
print()

