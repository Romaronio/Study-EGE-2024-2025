f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Теория\24.12.txt')
s = f.readline()
buff = ''
max_eval = 0
for i in range(len(s)):
	if s[i] in '789':
		buff += s[i]
		max_eval = max(max_eval, eval(buff))
	elif s[i] in '-*' and len(buff) > 0 and buff[-1] not in '-*':
		buff += s[i]
	elif s[i] == '0' and len(buff) > 0 and s[i - 1] not in '-*':
		buff += s[i]
		max_eval = max(max_eval, eval(buff))
	else: 
		buff = ''
print(max_eval)