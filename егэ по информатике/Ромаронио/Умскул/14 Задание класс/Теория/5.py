def f(a, n):
	return(sum(a[::-1][i] * n ** i for i in range(len(a))))
for x in range(9, 50):
	if f([2,2,2], x) + f([1, 7], 8) == f([2, 3, 8], 9):
		print(x)