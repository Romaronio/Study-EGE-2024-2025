def task(start, end):
	if start > end:
		return 0
	if start == end:
		return 1
	if start < end:
		return task(start + 1, end) + task(int(str(start) + '1'), end)
print(task(1, 928))