def g(s, x, p, end):
	if s + x >= 89 and p == end:
		return True
	if s + x < 89 and p == end:
		return False
	if s + x >= 89 and p != end:
		return False
	if (p + 1) % 2 == end % 2:
		return g(s + 2, x, p + 1, end) or g(s, x + 2, p + 1, end) or g(s * 3, x, p + 1, end) or g(s, x * 3, p + 1, end)
	else:
		return g(s + 2, x, p + 1, end) and g(s, x + 2, p + 1, end) and g(s * 3, x, p + 1, end) and g(s, x * 3, p + 1, end)
for s in range(1, 100):
	if g(s, 10, 0, 3) and not(g(s, 10, 0, 1)):
		print(s)