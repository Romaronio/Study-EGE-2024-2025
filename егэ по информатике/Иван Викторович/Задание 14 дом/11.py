k = 0
for n in range(2, 11):
	x = 572
	s = ''
	while x:
		s = str(x % n) + s
		x //= n
	print(s, n) 
m = 2 + 3 + 4 + 7
print(m)