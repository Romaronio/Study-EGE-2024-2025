for a in range(1, 1000):
	a_podoshel = True
	for x in range(1, 1000):
		for y in range(1, 1000):
			if ((17 * x - 3 * y + 17 != 0) or (a < x) or (a < y)) == False:
				a_podoshel = False
				break
		if a_podoshel == False:
			break
	if a_podoshel:
		print(a)
