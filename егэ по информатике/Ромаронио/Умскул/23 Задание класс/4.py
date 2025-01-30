def task(start, end):
	if start > end or start == 15 or start == 27:
		return 0
	if start == end:
		return 1
	if start < end:
		return task(start + 2, end) + task(start * 2, end)
print(task(3, 15) * task(15, 72) )