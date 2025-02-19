def task(start, end):
  if start > end:
    return 0
  if start == end:
    return 1
  if start < end:
    return task(start + 1, end) + task(start * 2, end)

print(task(2, 8) * task(8, 17) * task(17, 39))
