def seven(s):
	m = []
	while s:
		m.append(s % 7)
		s //= 7
	return m
for x in range(1, 2030):
	s = 7 ** 91 + 7 ** 160 - x
	if seven(s).count(0) == 70:
		print(x)