def f(a, n):
	return(sum(a[::-1][i] * n ** i for i in range(len(a))))
for p in range(7, 100):
	for x in range(p):
		for y in range(p):
			if f([1, x, 7, 7], p) + f([x, x, 7, 7], p) == f([y, 0, y, y], p):
				print(f([y, x, y, x], p))