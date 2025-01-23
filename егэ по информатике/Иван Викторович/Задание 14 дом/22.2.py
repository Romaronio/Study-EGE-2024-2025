mins = []
alfa = '0123456789abc'
for x in alfa:
	for y in alfa:
		res = int(f'8{x}78{y}', 13) + int(f'79{x}{y}7', 18)
		if res % 9 == 0:
			mins.append(res)
print(min(mins) // 9)