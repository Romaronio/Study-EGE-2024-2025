s = 3 * 289 ** 2024 + 81 * 49 ** 121 - 9 * 16 ** 81 - 6011
k = 0
while s:
	if s % 31 <= 17:
		k += s % 31
	s //= 31
print(k)