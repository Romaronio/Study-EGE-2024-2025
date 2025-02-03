s = 1000000
q1 = 1.1
q2 = 1.05
for x in range(1, 1000):
	Semen = (((s * q1 + x) * q1 + x) * q2 + x)
	Matvey = ((s * q1) * q1) + 2 * x * q2
	if round((Semen - Matvey)) % 2 == 0:
		print(x)
		break