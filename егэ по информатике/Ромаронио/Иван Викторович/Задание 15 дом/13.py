def f(x):
	return (a % 7 == 0) and ((240 % x == 0) <= ((a % x != 0) <= (780 % x != 0)))
k = 0
for a in range(1, 1001):
	if all(f(x) for x in range(1, 1000)):
		k += 1
print(k)