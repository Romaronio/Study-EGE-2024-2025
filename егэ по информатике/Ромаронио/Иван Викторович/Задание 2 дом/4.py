print('a b c')
for a in range(2):
	for b in range(2):
		for c in range(2):
			if (a and (not c)) or ((not a) and b and c):
				print(a, b, c)