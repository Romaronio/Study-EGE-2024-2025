def Del(n, m):
	return n % m == 0
B = list(range(70, 80))
a = list(range(1, 100))
i = []
for x in range(1, 1000):
	if Del(x, 12) and (x in B) and (not(Del(x, a))) == 0:
		i.append(a)
	print(a)

