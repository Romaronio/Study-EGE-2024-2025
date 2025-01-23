def f(a, n):
	return(sum(a[::-1][i] * n ** i for i in range(len(a))))
for x in range(0, 16):
	res = f([2, x, 8, 4], 19) + f([2, 1, 3, x], 16)
	if res % 88 == 0:
		print(res // 88)