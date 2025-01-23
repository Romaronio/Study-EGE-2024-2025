def task(start, end):
	if start < end or start == 32:
		return 0
	if start == end:
		return 1
	if start > end:
		return (start - 3, end) + (start // 2, end) + (start - 5, end)
print(task(43, 16)) 