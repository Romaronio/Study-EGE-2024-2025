for a in range(1, 1000):
	a_podoshel = 1
	for x in range(1, 1000):
		if (((x & 10 == 0) or (x & 12 != 0 )) or ((x & 30 != 0) <= (x & a == 0))) == False:
			a_podoshel = 0
			break
	if a_podoshel == 1:
		print(a)