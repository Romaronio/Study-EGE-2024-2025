def f(x, y):
	return (3 * x + 2 * y > 25) or (x > 2 * y) or (x + 4 * y < a)
for a in range(100, -1, -1):
	if all(f(x, y) for x in range(1000) for y in range(1000)) == 0:
		print(a)
		break