f = open(r'D:\Умскул\9 Задание класс\1.txt')
k = 0
for s in f:
	a = list(map(int, s.split()))
	# if a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
	if len(set(a)) != 3:
		k += 1
print(k)


