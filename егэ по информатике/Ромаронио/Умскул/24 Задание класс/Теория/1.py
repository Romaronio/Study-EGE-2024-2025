f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Теория\24.1.txt')
s = f.readline()
print(len(max(s.split('Q'), key=len)))