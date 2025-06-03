# Математик Артур продолжает оцифровывать старинные книги по математике. Данные сохраняются в текстовый файл, где каждая строка может содержать числа, символы математических операций (+, *, -), а также латинские буквы и служебные символы (#, &, @ и т. д.).

# Корректной считается строка, которая состоит только из десятичных чисел и математических операций (+, *, -). Стоит заметить, что из-за особенностей старинных счёта древнего племени Баговобоев, операции с отрицательными числами считаются некорректными. Если в строке обнаруживается минус, связанный с отрицательным числом, вся часть с отрицательным числом должна быть удалена перед вычислением.

# Помогите Артуру определить максимальное значение корректного математического выражения среди строк файла после удаления всех частей с отрицательными числами. В ответе укажите данное значение в виде целого числа.

# Пример: строка "-213*121+121-5*3", а значит для ее анализа она должна стать строкой вида "121+121*3", а значит значение выражение равно 484.

# f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24.txt Задание класс\Домашка\24.txt.14.txt')
# buff = ''
# res_mas = []
# def Minus(chislo):
# 	print(type(chislo))
# 	for i in range(len(chislo)):
# 		if chislo[i] in '-':
# 					for k in range(len(chislo)):
# 						if i + k - 1 < len(chislo) :
# 								chislo = chislo[:i] + chislo[i + k:]
# 					else:
# 						return chislo
# print(Minus('10000*222-22123+10'))
# for i, s in enumerate(f, start=1):
# 	try:
# 		if s[i] in '-':
# 				for k in range(1, 100):
# 					if s[i + k] not in '+*':
# 						s = s[:i] + s[i + k + 1:]
# 					else:
# 						break
# 		elif eval(s):
# 			if s[i].isdigit():
# 				buff += s[i]
# 				res_mas.append(eval(buff))
# 			elif s[i] in '-*+' and len(buff) > 0 and buff[-1] not in '-*+':
# 				buff += s[i]
# 			elif s[i] == '0' and len(buff) > 0 and buff[-1] not in '-*+':
# 				buff += s[i]
# 				res_mas.append(eval(buff))
# 	except:
# 		pass
# print(res_mas)

def clean_minus(s):
    if s[0] == '-':
        stop = min([i for i in range(len(s)) if s[i] in '*+'] + [len(s)]) + 1
        return s[stop:]
    start = s.index('-')
    stop = min([i for i in range(len(s)) if s[i] in '*+' and i > start] + [len(s)])
    return s[:start] + s[stop:]
f = open(r"C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Домашка\24.14.txt")
ans = []
available = '0123456789*+-'
for s in f:
    try:
        s = s.strip()
        if all(x in available for x in s):
            input_s = s
            while '-' in s:
                s = clean_minus(s)
            ans.append([eval(s), input_s])
    except:
        continue
print(max(ans))

