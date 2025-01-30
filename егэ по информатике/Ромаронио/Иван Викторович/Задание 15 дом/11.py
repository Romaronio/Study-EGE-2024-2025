def f(x):
	return ((x % 40 == 0) or (x % 64 == 0)) <= (x % a == 0)
for a in range(100000, 0, -1):
	if all(f(x) for x in range(10000)):
		print(a)
		break