def f(a, n):
	return(sum(a[::-1][i] * n ** i for i in range(len(a))))
for x in range(6, 130):
	res = f([2, 3, x, 3, 2], 130) + f([3, x, 2, 5, 3], 130)
	if res % 23 == 0:
		print(res // 23)