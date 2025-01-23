f = open(r'D:\Умскул\17 Задание класс\3.txt')
a = []
for s in f:
	a.append(int(s))
res_mas = []
for i in range(len(a) - 1):
	if a[i] * a[i + 1] % 74 == 0:
		res_mas.append(a[i] + a[i + 1])
print(len(res_mas), max(res_mas))
