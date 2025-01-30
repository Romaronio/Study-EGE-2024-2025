k = 0
for x in range(10000, 100000):
	s = str(x)
	if s[0] not in '01357' and s[-1] not in '26' and s.count('7') <= 2 and '9' not in s:
		k += 1
print(k)

