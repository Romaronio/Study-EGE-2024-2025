s = 234 ** 123 + 32 ** 12 - 32
m = 0
while s > 0:
	if s % 4 == 3:
		m += 1
	s //= 4
print(m)