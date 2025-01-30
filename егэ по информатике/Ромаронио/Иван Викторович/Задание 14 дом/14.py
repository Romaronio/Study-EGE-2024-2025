def five(a):
	s = ''
	while a:
		s = str(a % 5) + s
		a //= 5
	return s
for x in range(8300, 10000000):
	res = five(5 ** 100 - x)
	if res.count('0') == 4:
		print(x)
		break