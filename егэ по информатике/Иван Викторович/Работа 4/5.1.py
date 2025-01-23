for n in range(1, 100):
	s = bin(n)[2:]
	s = s + str(s.count('1') % 2)
	s = s + str(s.count('1') % 2)
	if int(s, 2) > 123:
		print(int(s, 2))
		break