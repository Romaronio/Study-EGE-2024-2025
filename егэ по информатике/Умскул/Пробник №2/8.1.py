k = 0
for n in range(10000, 100000):
	s = oct(n)[2:]
	if s.count('4') == 2:
		if '14' not in s or '34' not in s or '54' not in s or '74' not in s or '94' not in s or '41' not in s or '43' not in s or '45' not in s or '47' not in s or '49' not in s:
			k += 1
print(k)