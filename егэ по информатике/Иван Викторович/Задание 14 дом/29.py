def f(a, n):
	return(sum(a[::-1][i] * n ** i for i in range(len(a))))
for p in range(7, 100):
	for x in range(p):
		for y in range(p):
					if f([1, 6, 1], p) * f([5, 6], p) == f([5, x, y, 6], p):
						print(f([y, x], p), p)
						