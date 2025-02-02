f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Домашка\24.6.txt')
s = f.readline()
# s = s.split('YYZX')
# print(len(max(s, key=len)) + 6)

s = s.replace('YYZX', 'YYZ YZX')
s = s.split()
print(len(max(s, key=len)))