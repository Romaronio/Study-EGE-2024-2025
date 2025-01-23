def F(n):
	if n == 1:
		return 1
	if n % 2 == 0 and n > 1:
		return F(n - 1) + 7
	if n % 2 != 0 and n > 1:
		return F(n - 2) + 4 * n
print(F(100))