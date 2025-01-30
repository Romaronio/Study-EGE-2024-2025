def f(x, y):
	return (x * y < a) or (x >= 16) or (x < 5 * y)
for a in range(1000):
	if all(f(x, y) for x in range(1000) for y in range(1000)):
		print(a)
		break