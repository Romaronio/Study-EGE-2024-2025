def three(a):
	s = ''
	while a:
		s = str(a % 3) + s
		a //= 3
	return s

for x in range(2030, 0, -1):
	n = 3 **100 - x
	res = three(n)
	if res.count('0') == 5:
		print(x)
		break