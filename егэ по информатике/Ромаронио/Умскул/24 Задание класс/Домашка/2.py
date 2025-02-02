f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Домашка\24.2.txt')
s = f.readline()
s = s.split('Y')
print(len(max(s, key=len)))