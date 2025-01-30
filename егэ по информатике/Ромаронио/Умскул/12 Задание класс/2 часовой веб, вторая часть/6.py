def is_prime(x):
	for i in range(2, x): #функция котрая проверяет простое число или нет
		if x % i == 0:
			return False
	return True

for n in range(2, 1000):
	s = '>' + '0' * 21 + '1' * n + '2' * 13
	while '>1' in s or '>2' in s or '>0' in s:
		if '>1' in s:
			s = s.replace('>1', '22>', 1)
		if '>2' in s:
			s = s.replace('>2', '2>', 1)
		if '>0' in s:
			s = s.replace('>0', '1>', 1)
		# summ = s.count('1') * 1 + s.count('2') * 2
		# print(s)
	summ = sum(map(int, s[:-1]))
	if summ % n == 0:
		print(n, is_prime(n))
		break
		