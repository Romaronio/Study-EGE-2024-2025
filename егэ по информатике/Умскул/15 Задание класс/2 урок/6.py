for a in range(1, 1000):
	for x in range(1, 1000):
		if (((x & 14 != 0) or (x & 64 != 0)) <= ((x & 23 == 0) <= (x & a != 0))) == 0:
			break
	else:
		print(a)
		break