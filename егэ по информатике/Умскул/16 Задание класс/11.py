f = [0] * 10000
for n in range(10000):
	if n == 1:
		f[n] = 1
	if n > 1:
		f[n] = n ** 3 + f[n - 1]
print(f[2024] - f[2020])