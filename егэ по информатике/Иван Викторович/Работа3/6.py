for n in range(1, 100):
	s = bin(n)[2:]
	if s.count('1') > s.count('0'):
		s += '1'
	else:
		s += '0'
	if int(s, 2) < 90:
		print(int(s, 2))