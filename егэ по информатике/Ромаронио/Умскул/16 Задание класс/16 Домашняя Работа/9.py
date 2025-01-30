f = [0] * 10000
for n in range(10000):
	if n == 1:
		f[n] = 1
	if n > 1:
		f[n] = n * f[n - 1]
print((2026 * f[2029] + f[2028]) // f[2027])