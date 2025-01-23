for a in range(1000, 1, -1):
	for x in range(1, 1000):
		if ((x & a != 0) <= ((x & 21 == 0) <= (x & 66 != 0))) == 0:
			break
	else:
		print(a)
		break