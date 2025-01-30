s = '1' + '4' * 81
while '14' in s or '244' in s or '3444' in s:
	if '14' in s:
		s = s.replace('14', '3', 1)
	if '244' in s:
			s = s.replace('244', '1', 1)
	if '3444' in s:
			s = s.replace('3444', '2', 1)
print(s)