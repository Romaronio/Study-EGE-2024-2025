def f(a, n):
	return(sum(a[::-1][i] * n ** i for i in range(len(a))))
for x in range(9, -1, -1):
	res = f([1, 0, 1], int(f'12{x}34')) + f([1, 1, 1], int(f'124{x}3'))
	if res % 30 == 0:
		print(res // 30)