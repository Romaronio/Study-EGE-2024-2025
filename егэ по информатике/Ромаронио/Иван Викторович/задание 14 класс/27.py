def f(a, n):
	return(sum(a[::-1][i] * n ** i for i in range(len(a))))
for p in range(10, 100):
	for x in range(p):
		for y in range(p):
			for z in range(p):
				for w in range(p):
					if f([z, x, y, x, 9], p) + f([x, y, 7, 4, 8], p) == f([w, z, x, 6, 1], p):
						print(f([x, y, z, w], p))
						break