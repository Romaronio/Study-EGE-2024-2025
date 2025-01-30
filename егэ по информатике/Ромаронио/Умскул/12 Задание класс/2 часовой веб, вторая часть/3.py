for n in range(5555 + 1, 0, -1):
	s = '2' * n
	while '222' in s:
		s = s.replace('222', '5', 1)
		s = s.replace('555', '2', 1)
	if s == '5522':
		print(n)
		break