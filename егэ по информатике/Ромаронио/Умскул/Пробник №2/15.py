def Del(n, m):
	return n % m == 0
for a in range(1, 1000):
	a_podoshe = 1
	for x in range(1, 1000):
		if Del(x, a) <= (not(Del(x, 28)) or Del(x, 42)) == 0:
			a_podoshe = 0
			break
	if a_podoshe == 1:
		print(a)
			