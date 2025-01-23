maxmum = 0
f = []
def nine(a):
	s = ''
	while a: 
		s = str(a % 9) + s
		a //= 9
	return s
for x in range(2000):
	res = nine(9 ** 250 + 9 ** 150 - x)
	if maxmum <= res.count('1'):
		maxmum = res.count('1')
		f = x
		print(x)