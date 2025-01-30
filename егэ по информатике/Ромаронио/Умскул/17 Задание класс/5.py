f = open(r'D:\Умскул\17 Задание класс\5.txt')
a = []
for s in f:
	a.append(int(s))
res_mas = []
for i in range(len(a) - 1):
	if a[i] > 0 and a[i] ** (1/2) % 1 == 0 or a[i + 1] > 0 and a[i + 1] ** (1/2) % 1 == 0:
		res_mas.append(a[i] + a[i + 1])
print(len(res_mas), max(res_mas))


