s = '>' + '2' * 40 + '3' * 40 + '5' * 20
while '>2' in s or '>3' in s or '>5' in s:
	if '>2' in s:
		s = s.replace('>2', '33>', 1)
	if '>3' in s:
		s = s.replace('>3', '3>', 1)
	if '>5' in s:
		s = s.replace('>5', '2>', 1)
# a = 0
# for i in s[:-1]: #первый интуитовно понятный способ
# 	a = a + int(i)
# print(a)

# summ = [int(i) for i in s[:-1]] #второй способ через генератор списков
# print(sum(summ))

print(sum(map(int, s[:-1]))) #через map, но главное помнить, что int передаем без (), не int(), а int

