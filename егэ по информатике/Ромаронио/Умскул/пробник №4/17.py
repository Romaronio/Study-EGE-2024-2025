f = open('17.txt')
s = f.read()
s = s.split()
k = 0
mas = []
for i in range(len(s) - 1):
  if (int(s[i]) + int(s[i + 1])) % 4 == 0 and (int(s[i]) + int(s[i + 1])) % 7 != 0:
    if str((int(s[i]) * int(s[i + 1])))[-1] == '3':
      mas.append([int(s[i]), int(s[i + 1])])
      k += 1
sum_mas = 10**10
for i in mas:
  if sum(i) < sum_mas:
    sum_mas = sum(i)

print(k, sum_mas)
