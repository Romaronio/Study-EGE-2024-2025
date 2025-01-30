def F(n):
	if n == 1:
		return 1
	if n > 1:
		return G(n - 1) + 3 * F(n - 1) - 5 * n + 1
def G(n):
	if n == 1:
		return 1
	if n > 1:
		return 2 * F(n - 1) - G(n - 1) + 4 * n - 2
print(G(12))