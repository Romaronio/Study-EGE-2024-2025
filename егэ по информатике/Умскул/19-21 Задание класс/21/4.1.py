def g(s, p, end):
	if s >= 88 and p in end:
		return True
	if s < 88 and p == max(end):
		return False
	if s >= 88 and p not in end:
		return False
	movies = [g(s + 2, p + 1, end), g(s + 3, p + 1, end), g(s * 2, p + 1, end)]
	if (p + 1) % 2 == end[0] % 2:
		return any(movies)
	else:
		return all(movies)
for s in range(1, 88):
	if g(s, 0, [2,4]) and not(g(s, 0, [2])):
		print(s)