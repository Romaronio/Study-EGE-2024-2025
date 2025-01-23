def task(start, end):
	if start > end or start == 44:
		return 0
	if start == end:
		return 1
	if start < end:
		return task(start + 2, end) + task(start * 3, end)
print(task(2, 24) * task(24, 144))