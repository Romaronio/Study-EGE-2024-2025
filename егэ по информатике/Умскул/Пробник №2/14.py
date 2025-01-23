s = 25 ** 125 - 125 ** 10 * 25 ** 20 + 5 ** 5 - 5
a = []
while s > 0:
	a.append(s % 5)
	s = s // 5
print(a.count(0))