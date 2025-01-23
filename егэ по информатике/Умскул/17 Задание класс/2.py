f = open(r'D:\Умскул\17 Задание класс\2.txt')
a = []
for s in f:
	a.append(int(s))
res_mas = []
for i in range(len(a) - 1):
	if a[i] > 1234 or a[i + 1] > 1234:
		res_mas.append(a[i] * a[i] + a[i + 1] * a[i + 1])
print(len(res_mas), max(res_mas))