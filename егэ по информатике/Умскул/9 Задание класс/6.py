f = open(r'D:\Умскул\9 Задание класс\6.txt')
k = 0
for s in f:
	a = sorted(map(int, s.split()))
	povtor = [x for x in a if a.count(x) > 1]
	nepovtor = [x for x in a if a.count(x) == 1]
	if len(povtor) == 3 and (sum(povtor) ** 2 > sum(nepovtor) ** 2):
		k += 1
print(k)
# from itertools import *
# for i in product([0, 1, 2, 3, 4], ['a', 'b'], repeat=5):
# 	print(i)
# # for i in permutations([0, 1, 2, 3, 4], r=5):
# # 	print(i)