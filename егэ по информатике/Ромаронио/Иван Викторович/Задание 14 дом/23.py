def f(a, n):
	return(sum(a[::-1][i] * n ** i for i in range(len(a))))
for x in range(10, 123):
	res = f([1, 2, x, 4, 5], 98) + f([1, x, 9, 8], 123)
	if res % 123 == 0:
		print(res // 123)