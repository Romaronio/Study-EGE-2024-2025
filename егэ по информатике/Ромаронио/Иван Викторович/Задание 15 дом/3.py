def f(x, y):
	return (y + 5 * x != 80) or (3 * x > a) or (y > a)
for a in range(1000, -1, -1):
	if all(f(x, y) for x in range(1000) for y in range(1000)):
		print(a)
		break