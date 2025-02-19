import string
for x in '1234567890abcd':
	for y in '1234567890abcd':
		s = int(f'ABCD3{y}2{x}1', 14) + int(f'192{x}9', 14) % 107
		if s % 107 == 0:
			print(x, y, s // 107)
