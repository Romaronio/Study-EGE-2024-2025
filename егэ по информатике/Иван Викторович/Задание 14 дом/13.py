def seven(a):
	s = ''
	while a:
		s = str(a % 7) + s
		a //= 7
	return s
for x in range(3000, 1, -1):
	n = 7 ** 100 - x
	res = seven(n)
	if res.count('0') == 2:
		print(x)
		break
