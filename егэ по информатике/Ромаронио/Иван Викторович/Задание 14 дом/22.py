def f(a, n):
	return(sum(a[::-1][i] * n ** i for i in range(len(a))))
for x in range(10, 19):
	res = f([9, 8, 8, 9, 7, x, 2, 1], 19) + f([2, x, 9, 2, 3], 19)
	if res % 18 == 0:
		print(res // 18)