x = 12 ** 34 + 7 * 12 ** 26 - 3 * 12 ** 16 + 2 * 12 ** 5 + 552
s = set()
while x:
	s.add(x % 12)
	x = x // 12
print(len(s))