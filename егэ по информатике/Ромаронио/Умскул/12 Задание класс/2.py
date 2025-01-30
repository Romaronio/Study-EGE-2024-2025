s = '1' * 9 + '2' * 22
while '111' in s or '222' in s:
	while '111' in s:
		s = s.replace('111', '2', 1)
	while '222' in s:
		s = s.replace('222', '1', 1)
print(s)