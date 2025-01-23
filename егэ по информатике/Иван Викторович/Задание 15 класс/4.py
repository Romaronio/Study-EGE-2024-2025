def f(x):
	return (x & 53 == 0) <= ((x & 19 != 0) <= (x & a != 0))
for a in range(1000):
	if all(f(x) for x in range(1, 1000)):
		print(a)
		break
	