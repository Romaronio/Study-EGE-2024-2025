for a in range(1, 1000):
	if all(((x & 13 != 0) or (x & 12 != 0)) <= ((x & 26 == 0) <= (x & a != 0)) for x in range(1, 1000)) == True:
		print(a)
		break