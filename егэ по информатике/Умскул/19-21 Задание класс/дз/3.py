def g(s, p, end):
	if s >= 51 and p == end:
		return True
	if s < 51 and p == end:
		return False
	if s >= 51 and p != end:
		return False
	if (p + 1) % 2 == (end % 2):
		return g(s + 1, p + 1, end) or g(s * 2, p + 1, end)
	else:
		return g(s + 1, p + 1, end) and g(s * 2, p + 1, end)
for s in range(1, 52):
	if g(s, 0, 2):
		print(s)