f = open(r'D:\Умскул\9 Задание класс\2.txt')
k = 0
for s in f:
	a = list(map(int, s.split()))
	for i in range(len(a) - 2):
		if (sum(a) // 3) < 30:
			k += 1
print(k, a)