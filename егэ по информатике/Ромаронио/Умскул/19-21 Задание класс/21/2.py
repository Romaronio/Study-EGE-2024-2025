def g(s, p, end):
	if s >= 93 and p in end:
		return True
	if s < 93 and p == max(end):
		return False
	if s >= 93 and p not in end:
		return False
	if (p + 1) % 2 == (end[0] % 2):
		return g(s + 1, p + 1, end) or g(s * 3 - 1, p + 1, end)
	else:
		return g(s + 1, p + 1, end) and g(s * 3 - 1, p + 1, end)	
for s in range(1, 94):
	if g(s, 0, [2, 4]) and not(g(s, 0, [2])):
		print(s)