def F(n):
	if n == 1:
		return 3
	if n > 1:
		return 4 * F(n -1) -3 * n
print(F(5))