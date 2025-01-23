def Del(n, m):
	return n % m == 0
for a in range(1, 1000):
	a_podoshel = 1
	for x in range(1, 10000):
		if ((Del(x, a) and Del(x, 24)) <= Del(x, 36)) == 0:
			a_podoshel = 0
			break
	if a_podoshel == 1:
		print(a)
		break
	


