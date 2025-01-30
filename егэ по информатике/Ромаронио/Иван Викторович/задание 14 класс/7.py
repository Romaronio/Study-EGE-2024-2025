for n in range(2, 11):
	x = 364
	s = set()
	while x:
		s.add(x % n)
		x //= n
	if len(s) == 1:
		print(n, s)


