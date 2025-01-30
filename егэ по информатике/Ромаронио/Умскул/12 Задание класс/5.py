s = '123' * 456
while '12' in s:
	s = s.replace('12', '3', 1)
	s = s.replace('3333', '3', 1)
print(s)