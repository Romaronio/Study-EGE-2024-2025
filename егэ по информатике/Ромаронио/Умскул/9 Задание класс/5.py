f = open(r'D:\Умскул\9 Задание класс\5.txt')
k = 0
for s in f:
	a = sorted(map(int, s.split()))
	povtor = [x for x in a if a.count(x) > 1]
	nepovtor = [x for x in a if a.count(x) == 1]
	if (len(nepovtor) == 3 and len(set(povtor)) == 2) and (sum(povtor) / len(povtor) < (sum(a) / len(a))):
		k += 1
print(k)

