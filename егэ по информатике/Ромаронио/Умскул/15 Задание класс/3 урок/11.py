for a in range(1, 1000):
	if all(((2 * x - y < a) or ((x > 55) or (y > 32)) for x in range(0, 1000) for y in range(0, 1000))) == True:
				print(a)
				break