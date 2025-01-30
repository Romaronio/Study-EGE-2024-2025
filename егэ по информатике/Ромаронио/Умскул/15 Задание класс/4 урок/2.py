p = list(range(16, 60))
q = list(range(27, 72))
a = []
for x in range(1, 100):
	if ((not(x in a)) <= ((x in p) <= (not(x in q)))) == 0:
		a.append(x)
print(a, 59 - 27)