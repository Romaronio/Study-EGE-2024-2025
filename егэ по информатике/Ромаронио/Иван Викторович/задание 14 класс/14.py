def three(a):
	s = ''
	while a:
		s = str(a % 7) + s
		a //= 7
	return s

for x in range(5001, 100000000):
	n = 7 **100 - x
	res = three(n)
	if res.count('0') == 5:
		print(x)
		break