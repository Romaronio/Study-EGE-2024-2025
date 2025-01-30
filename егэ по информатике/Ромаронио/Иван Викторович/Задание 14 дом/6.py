x = 9 ** 8 + 3 ** 25 - 14
s = 0
while x: 
	s += x % 3
	x //= 3
print(s)