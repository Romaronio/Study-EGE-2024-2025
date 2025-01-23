def f(x):
	return (x in range(160, 181)) <= ((x % 35 == 0) <= (x % a == 0))
k = 0
for a in range(1, 1000):
	if all(f(x) for x in range(1, 1000)):
		k += 1
print(k)