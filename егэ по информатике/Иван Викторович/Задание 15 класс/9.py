def f(x):
	return (a % 35 == 0) and ((730 % x == 0) <= ((a % x != 0) <= (110 % x != 0)))


k = 0
for a in range(1, 1001):
	if all(f(x) for x in range(1, 1000)):
		k += 1
print(k)