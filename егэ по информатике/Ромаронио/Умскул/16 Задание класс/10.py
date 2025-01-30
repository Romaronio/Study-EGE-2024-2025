f = [0] * 10000
for n in range(10000):
	if n == 1:
		f[n] = 1
	if n > 1:
		f[n] = n * f[n - 1]
print(f[2023] / f[2021])
