def three(a, n):
	return sum(a[::-1][i] * n ** i for i in range(len(a)))
for x in range(1, 100):
	if three([1, 6, 5], x) + int('18', 9) == int('416', 7):
		print(x)