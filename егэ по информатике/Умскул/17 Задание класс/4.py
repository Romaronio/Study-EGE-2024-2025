f = open(r'D:\Умскул\17 Задание класс\4.txt')
a = []
for s in f:
	a.append(int(s))
res_mas = []
for i in range(len(a) - 2):
	if a[i] > 0 or a[i + 1] > 0 or a[i + 2] > 0:
		res_mas.append(a[i] + a[i + 1] + a[i + 2])
print(len(res_mas), min(res_mas))