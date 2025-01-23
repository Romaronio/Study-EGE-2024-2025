from string import *
alfa = digits + ascii_lowercase
a = []
for x in range(7, 14):
	for y in range(9, x):
		s = int(f'5{alfa[x]}37{alfa[y]}', 14) + int(f'10{alfa[y]}63', x) - int('35148', y)
		a.append([s, x, y, s // (x + y)])
print(max(a))
