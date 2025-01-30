k = 0
for n in range(1, 10000):
	s = '1' * n + '2' * n
	while '111' in s or '22' in s:
		s = s.replace('111', '2', 1)
		s = s.replace('222', '1', 1)
		s = s.replace('221', '1', 1)
		s = s.replace('122', '1', 1)
		s = s.replace('22', '2', 1)
	print(s)
	if s.count('2') == 9:
		k += 1
	print(k)
