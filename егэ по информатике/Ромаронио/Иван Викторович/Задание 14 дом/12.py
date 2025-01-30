x = 81 ** 79 + 75 ** 2022 - 12 ** 35
s = ''
while x: 
	s = str(x % 5) + s
	x //= 5
m = s.count('41') + s.count('42') + s.count('43')
print(m)