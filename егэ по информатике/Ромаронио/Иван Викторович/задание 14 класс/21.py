alfa = '0123456789ab'
for x in alfa:
	for y in alfa:
		f = int(f'{y}AA{x}', 12) + int(f'{x}02{y}', 14)
		if f % 80 == 0:
			print(f, f//80)