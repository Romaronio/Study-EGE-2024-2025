def f(a, n):
	return(sum(a[::-1][i] * n ** i for i in range(len(a))))
for x in range(10, 19):
	res = f([9, 8, x, 7, 9, 6, 4, 1], 19) + f([3, 6, x, 1, 4], 19) + f([7, 3, x, 4], 19)
if res % 18 == 0:
	print(res // 18)