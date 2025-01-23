from math import *
f = open(r'D:\Умскул\9 Задание класс\4.txt')
k = 0
for s in f:
	a = sorted(map(int, s.split()))
	if a[0] * a[1] * a[2] * a[3] < a[4] ** 2:
		if a[4] + a[3] / 2 > a[0] + a[1] + a[2]:
			k += 1
print(k)
