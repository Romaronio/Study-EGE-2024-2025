def g(s, x, p, end):
	if (x + s) >= 73: return p in end
	if (x + s) < 73 and p == max(end): return False
	movis = [g(s + 2, x, p + 1, end), g(s, x + 2, p + 1, end), g(s * 2, x, p + 1, end), g(s, x * 2, p + 1, end)]
	return any(movis) if (p + 1) % 2 == (end[0] % 2) else all(movis)
print([s for s in range(1, 69) if g(s, 4, 0, [1])])