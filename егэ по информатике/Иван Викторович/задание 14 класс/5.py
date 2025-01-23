x = 216 ** 6 + 216 ** 4 + 36 ** 6 - 6 **14 - 24	
k = set()
while x:
	s = x % 6
	k.add(s)
	x //= 6
print(k)