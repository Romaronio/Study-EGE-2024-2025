def F(n):
	if n > 15:
		return n * 2
	if n <= 15:
		return 2 * F(n + 2) + 4 * n
print(F(7))