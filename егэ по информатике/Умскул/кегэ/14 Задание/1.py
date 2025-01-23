s = 729 ** 8 - 3 ** 18 + 85
def nine(a, n):
	return sum(a[::-1][i] * n ** i for i in range(len(a)))
m = nine([s], 9)
print(str(m).count('0'))