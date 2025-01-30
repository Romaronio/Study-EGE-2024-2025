x = 343 ** 5 + 343 ** 4 + 49 ** 6 - 7 ** 13 - 21
s = set()
while x:
	s.add(x % 7)
	x //= 7
print(len(s))