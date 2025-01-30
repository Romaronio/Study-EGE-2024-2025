s = 234 ** 123 + 32 ** 12 - 32
m = []
while s > 0:
	m.append(s % 4)
	s //= 4
print(m.count(3))