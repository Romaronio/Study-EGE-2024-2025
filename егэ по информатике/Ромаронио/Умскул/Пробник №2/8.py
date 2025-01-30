k = 0
for n in range(10000, 100000):
	s = oct(n)[2:]
	if s.count('4') == 2:
		if (int(s[s.index('4') - 1]) % 2 == 0 and int(s[s.index('4') - 1]) % 2 == 0):
			k += 1
		print(k)