def g(s, p, end):
	if s >= 37 and p == end:
		return True
	if s < 37 and p == end:
		return False
	if s >= 37 and p != end:
		return False
	if (p + 1) % 2 == end % 2:
		return g(s + 1, p + 1, end) or g(s * 2, p + 1, end)
	else:
		return g(s + 1, p + 1, end) and g(s * 2, p + 1, end)
for s in range(1, 37):
	if (g(s, 0, 3) and not(g(s, 0, 1))):
		print(s)