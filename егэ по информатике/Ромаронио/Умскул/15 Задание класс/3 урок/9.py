for a in range(1, 1000):
	a_podoshel = 1
	for x in range(1, 1000):
		for y in range(1, 1000):
			if ((y - 13 * x < a) or (x > 88) or (y > 77)) == 0:
				a_podoshel = 0
				break
		if a_podoshel == 0:
			break
	if a_podoshel == 1:
		print(a)
		break