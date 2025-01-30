def three(a):
	s = ''
	while a:
		s = str(a % 5) + s
		a //= 5
	return s
s = 4 * 25 ** 2022 - 2 * 5 ** 2000 + 125 ** 1011 - 3 * 5 ** 100 - 660
b = three(s)
print(str(b).count('4'))