def f(x, y):
	return (3 * x + 2 * y > 95) or (4 * x < 3 * y) or (x + 4 * y < a)
for a in range(1000, -1, -1):
	if all(f(x, y) for x in range(300) for y in range(300)) == 0:
		print(a)
		break