x = 9 ** 7 + 3 ** 21 - 9
k = 0
while x:
	if x % 3 == 2:
		k += 1
	x //= 3
print(k)
