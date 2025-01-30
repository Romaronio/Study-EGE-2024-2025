a = []
for n in range(4, 1000):
	s = '5' + '2' * n
	while '52' in s or '2222' in s or '3322' in s:
		if '52' in s:
			s = s.replace('52', '33', 1)
		if '2222' in s:
			s = s.replace('2222', '5', 1)
		if '3322' in s:
			s = s.replace('3322', '25', 1)
	summ = s.count('2') * 2 + s.count('3') * 3 + s.count('5') * 5
	print(summ, n)
	# if summ == 83:
	# 	print(n)