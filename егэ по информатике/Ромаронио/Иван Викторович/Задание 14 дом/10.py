summ = 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
for n in range(2, 11):
	x = 1755
	s = ''
	while x:
		s = str(x % n) + s
		x //= n	