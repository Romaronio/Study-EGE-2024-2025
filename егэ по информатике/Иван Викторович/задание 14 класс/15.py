def five(a):
	s = ''
	while a:
		s = str(a % 5) + s
		a //= 5
	return s

maximum = 0
for x in range(2,2025):
	n = 5 ** 2025 + 5 ** 200 - x
	res = five(n)
	if res.count('4') >= maximum:
		maximum = res.count('4')
		f = x
print(f)