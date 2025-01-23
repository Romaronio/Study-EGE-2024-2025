def f(x):
	return (x % a == 0) or (x % 23 == 0) <= (x not in range(50, 70))
for a in range(100000, -1, -1):
	if all(f(x) for x in range(1, 100000)):
		print(a)
		break
