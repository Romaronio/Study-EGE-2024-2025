def g(s, x, p, end):
	if s + x >= 123 and p in end:
		return True
	if s + x < 123 and p == max(end):
		return False
	if s + x >= 123 and p not in end:
		return False
	if (p + 1) % 2 == end[0] % 2:
		return g(s + 1, x, p + 1, end) or g(s * 2, x, p + 1, end) or g(s, x + 1, p + 1, end) or g(s, x * 2, p + 1, end)
	else:
		return g(s + 1, x, p + 1, end) and g(s * 2, x, p + 1, end) and g(s, x + 1, p + 1, end) and g(s, x * 2, p + 1, end)
for s in range(1, 124):
	if g(s, 9, 0, [2, 4]) and not(g(s, 9, 0, [2])):
		print(s)