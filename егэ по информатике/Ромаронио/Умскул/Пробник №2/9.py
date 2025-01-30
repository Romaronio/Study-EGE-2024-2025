f = open(r'D:\Умскул\2 Пробник\9.txt')
k = 0
for s in f:
	a = sorted(map(int, s.split()))
	povtor = [x for x in a if a.count(x) > 1]
	nepovtor = [x for x in a if a.count(x) == 1]
	if len(set(povtor)) == 2:
		if sum(povtor) / len(povtor) < sum(nepovtor) / len(nepovtor):
			print()
print(k)
