f = open('16.txt')
mas = [int(s) for s in f]
mas_par = []
k = 0
mas_par_chis = []
max_mas_elem = [i for i in mas if str(i).count('1') + str(i).count('3') + str(i).count('5') + str(i).count('7') + str(i).count('9') == str(i).count('0') + str(i).count('2') + str(i).count('4') + str(i).count('6') + str(i).count('8')]
max_elem = max(max_mas_elem)
for i in range(len(mas) - 1):
    mas_par.append([str(mas[i]), str(mas[i + 1])])

for i in mas_par:
    mas_par_chis.append([[int(s) for s in i[0]], [int(s) for s in i[1]]])

for i in range(len(mas_par_chis)):
    if min(mas_par_chis[i][0]) > max(mas_par_chis[i][1]):
        if (int(mas_par[i][0]) + int(mas_par[i][0])) < 9980:
            k += 1

print(k)


