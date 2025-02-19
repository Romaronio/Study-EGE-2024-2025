f = [0] * 1000
for n in range(1000):
	if n < 2:
		f[n] = 1
	if n >= 2:
		f[n] = f[n - 1] * (n + 1)
print(f[15])
