s =  1296 ** 625 * 216 ** 125 + 36 ** 25 - 6 ** 5
k = 0
while s > 0:
	if s % 6 == 5:
		k += 1
	s //= 6
print(k)