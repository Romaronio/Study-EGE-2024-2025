k = 0
for n in range(1, 100):
	s = bin(n)[2:]
	s += str(s.count('1') % 2)
	s += str(s.count('1') % 2)
	if 90 <= int(s, 2) <= 160:
		k += 1
print(k)
