def f(start, end):
	if start == 26:
		return 0
	if start > end:
		return 0
	if start == end:
		return 1
	if start < end:
		return f(start + 2, end) + f(start * 2, end)
print(f(2, 14) * f(14, 56))