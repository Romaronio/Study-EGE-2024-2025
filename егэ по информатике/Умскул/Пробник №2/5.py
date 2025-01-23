for n in range(1, 1000):
	s = bin(n)[2:]
	s = s + s[-1:]
	if s.count('1') % 2 == 0:
		s = s + '0'
	else:
		s = s + '1'
	if s.count('1') % 2 == 0:
		s = s + '0'
	else:
		s = s + '1'
	if int(s, 2) >= 177:
		print(n)
		break