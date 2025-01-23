def f(a, n):
	return(sum(a[::-1][i] * n ** i for i in range(len(a))))
res = []
for p in range(10, 100):
	for x in range(p):
		for y in range(p):
					if f([7, 1, ], p) *  f([6, 9], p) == f([x, y, 9], p):
						res.append((p, f([y, x], p)))
print(min(res))