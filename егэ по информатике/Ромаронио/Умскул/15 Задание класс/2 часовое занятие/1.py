def Del(n, m):
	return n % m == 0
# def f(x, a):
# 	return (Del(x, a)) and (Del(x, 30)) <= (not(Del(x, 30)) or not(Del(x, 40)))
# for x in range(100):
# 	for a in range(100):
# 		if f(x, a) == 1:
# 			print(a)

for a in range(1, 1000):
	A_podoshel = 1
	for x in range(1, 1000):
		if ((Del(x, a) and Del(x, 30)) <= ((not(Del(x, 30))) or Del(x, 40))) == 0:
			A_podoshel = 0
			break
	if A_podoshel == 1:
		print(a)
		break

