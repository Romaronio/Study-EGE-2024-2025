f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Теория\24.2.txt')
s = f.readline()
a = s.split('R')
print(len(max(a, key=len)))