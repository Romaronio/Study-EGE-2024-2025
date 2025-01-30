def f(a, n):
	return sum(a[::-1][i] * n ** i for i in range(len(a)))

for p in range(9, 100):
	for x in range(p):
		for y in range(p):
			if f([7, 5], p) * f([8, 7], p) == f([1, x, y, 2], p):
				print(f([y, x], p))