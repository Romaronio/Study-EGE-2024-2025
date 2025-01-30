def Del(m, n):
	return m % n == 0
for a in range(1, 10000):
	A_podoshel = 1
	for x in range(1, 10000):
		if (Del(a, 4) and (not(Del(2024, a))) <= (Del(x, 1234)) <= Del(2022, a)) == 0:
			A_podoshel = 0
			break
	if A_podoshel == 1:
		print(a)