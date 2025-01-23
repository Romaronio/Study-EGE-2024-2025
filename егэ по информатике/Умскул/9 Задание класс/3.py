f = open(r'D:\Умскул\9 Задание класс\3.txt')
k = 0
for s in f:
	a = sorted(map(int, s.split()))
	if (max(a) + min(a)) % 3 == 0 and (abs(a[0] - a[1]) == abs(a[2] - a[3]) or abs(a[0] - a[2]) == abs(a[1] - a[3])):
		k += 1
print(k)
		
