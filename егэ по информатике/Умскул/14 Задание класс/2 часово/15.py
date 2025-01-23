def three(a, n):
	return sum(a[::-1][i] * n ** i for i in range(len(a)))
for x in range(150):
	s = three([5, 1, x, 2, 9], 150) + three([x, 0, 2, 3], 150)
	if s % 149 == 0:
			print(x, three([s], 150) // 149)