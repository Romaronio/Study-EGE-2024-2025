x = 2 * 216 ** 8 + 4 * 36 ** 12 + 6 ** 15 - 1296
m = ''
while x: 
	m = str(x % 6) + m
	s = m.count('0')
	x = x // 6
print(s)