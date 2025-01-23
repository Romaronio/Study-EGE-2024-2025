def Del(m, n):
	return m % n == 0
for a in range(1, 1000):
	a_podoshel = 1
	for x in range(1, 1000):
		if (Del(x, a) and Del(x, 24) and (not(Del(x, 16)))) <= (not(Del(x, a))) == 0:
			a_podoshel = 0
	if a_podoshel == 1:
		print(a)
		break