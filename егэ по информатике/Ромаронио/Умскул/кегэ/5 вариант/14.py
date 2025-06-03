def free(x):
  s = ''
  while x:
    s = str(x % 3) + s
    x = x // 3
  return s

for x in range(21, 30):
  if free(x)[-2:] == '11':
    print(free(x), x)
