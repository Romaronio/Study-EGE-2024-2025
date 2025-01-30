for a in range(1, 1000):
	a_podoshel = 1
	for x in range(1, 1000):
		for y in range(1, 1000):
			if (((x >= 17) or (3 * x < y)) or ((y * x < a))) == 0:
				a_podoshel = 0
				break
		if a_podoshel == 0:
			break
	if a_podoshel == 1:
		print(a)
		break