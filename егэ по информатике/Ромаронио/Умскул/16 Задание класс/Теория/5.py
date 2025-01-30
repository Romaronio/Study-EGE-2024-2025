def F(n):
	if n <= 4:
		return 0
	if n > 4 and n % 4 == 0:
		return F(n - 1) + 3 * n
	if n > 4 and n % 4 > 0:
		return F(n - (n % 4)) + 8 * n - 2
print(F(43))