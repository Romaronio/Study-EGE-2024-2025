import string
for x in '1234567890' + string.ascii_lowercase[:9]:
	k = int(f'98{x}79641', 19) + int(f'36{x}14', 19) + int(f'73{x}4', 19)
	if k % 18 == 0:
		print(x, k // 18)


