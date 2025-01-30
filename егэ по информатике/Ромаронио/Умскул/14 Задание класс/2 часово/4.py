x = 32 ** 2023 + 16 ** 2022 - 256 ** 101
k = set()
while x > 0:
	s = x % 18
	k.add(s)
	x //= 18
print(len(k))