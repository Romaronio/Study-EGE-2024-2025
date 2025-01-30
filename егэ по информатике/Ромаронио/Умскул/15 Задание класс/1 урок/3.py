def Del(n, m):
	return n % m == 0


for a in range(10000, 0, -1):
	a_podoshel = True
	for x in range(1, 10000):
		if ((not(Del(x, a))) <= (Del(x, 45) <= (not(Del(x, 75))))) == False:
			a_podoshel = False
			break
	if a_podoshel == True:
		print(a)
		break