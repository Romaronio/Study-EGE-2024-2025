for n in range(1, 200):
	s = bin(n)[2:]
	s = s + s[-1]
	s += str(bin(n).count('1') % 2)
	s += str(s.count('1') % 2)
	if int(s, 2) > 80:
		print(int(s, 2))
		break



