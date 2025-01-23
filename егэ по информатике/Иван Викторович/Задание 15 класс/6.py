def f(x):
	return ((x % 7 == 0) <= (x % 21 != 0)) or (2 * x + a >= 120)
for a in range(1, 1000):
	if all(f(x) for x in range(1, 1000)):
		print(a)
		break