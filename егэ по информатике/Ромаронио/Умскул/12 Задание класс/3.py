s = '5' + '4' * 99
while '54' in s or '644' in s or '7444' in s:
	if '54' in s:
		s = s.replace('54', '6', 1)
	else:
		if '644' in s:
			s = s.replace('644', '7', 1)
		else: 
			s = s.replace('7444', '5', 1)
print(s)