f = open(r'D:\Умскул\17 Задание класс\1.txt')
a = []
for s in f:
	a.append(int(s))
sum_par = []
for i in range(len(a) - 1):
	if a[i] % 11 == 0 and a[i + 1] % 11 == 0:
		sum_par.append(a[i] + a[i + 1])
print(len(sum_par), min(sum_par))

