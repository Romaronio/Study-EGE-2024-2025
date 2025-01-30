def f(a, n):
	return(sum(a[::-1][i] * n ** i for i in range(len(a))))
for p in range(9, 100):
	for x in range(p):
		for y in range(p):
			if f([4, x, 4, 6], p) + f([x, x, 1, 7], p) == f([y, 3, 8, 6, y], p):
				print(f([x, y, x, y], p))