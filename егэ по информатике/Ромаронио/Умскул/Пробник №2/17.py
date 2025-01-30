f = open(r'D:\Умскул\2 Пробник\17.txt')
a = []
for s in f:
	a.append(int(s))
res_mas = []
for i in range(len(a) - 1):
	if a[i - 1] < 0 or a[i] < 0 or a[i + 1] < 0:
		res_mas.append(a[i - 1] + a[i] + a[i + 1])
print(min(res_mas))