from itertools import *
k = 0
for x in product('0123456789abcde', repeat = 5):
	if x[0] != '0' and x.count('8') == 1 and len([i for i in x if i in'abcde']) >= 2:
		k+=1
print(k)
