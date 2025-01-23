x = 53 ** 123 + 65 ** 2222 - 172 ** 12
m = ''
while x:
	m = str(x % 7) + m
	x = x // 7
summ = m.count('61') + m.count('62') + m.count('63') + m.count('64') + m.count('65')
print(summ)