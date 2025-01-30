def f(x):
	return ((x & 32765 != 0) or (x & 22635 != 0)) <= (x & a >0)
for a in range(1000000):
	if all(f(x) for x in range(10000000)):
		print(a)
		break