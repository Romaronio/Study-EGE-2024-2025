f = [0] * 1000
for n in range(1000):
	if n <= 3:
		f[n] = 1
	if n > 3 and n % 3 == 0:
		f[n] = f[n // 3] + 4 * n
	if n > 3 and n % 3 != 0:
		f[n] = n * n * n - 26
	if f[n] < 300:
		print(n, f[n])
