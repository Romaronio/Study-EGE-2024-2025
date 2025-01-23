for a in range(1, 1000):
	a_podshodit = 1
	for x in range(1, 1000):
		if ((x & 79 != 0) <= ((x & 64 == 0) <= (x & a != 0))) == False:
			a_podshodit = 0
			break
	if a_podshodit == 1:
		print(a)
		break