def f(x):
	return (x % a != 0) <= ((x % 24 != 0) and (x % 36 != 0))
for a in range(100000, 0, -1):
	if all(f(x) for x in range(1, 1000)):
		print(a)
		break