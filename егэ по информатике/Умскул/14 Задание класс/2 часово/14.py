def three(a, n):
	return sum(a[::-1][i] * n ** i for i in range(len(a)))
for c in range(37):
	for d in range(37):
		s = three([4, 5, c, 7, 3, d, 9], 37)
		if s % 15 == 0:
			print(three([c, d], 37))
			