x = 9 ** 18 + 3 ** 54 - 9	
k = 0
while x:
	if x % 3 == 2:
		k += 1
	x//= 3
print(k)