f = open('24_1.txt')
s = f.readline()
s = s.replace('++', ' ').replace('**', ' ').replace('+*', ' ').replace('*+', ' ')
s = [i for i in s.split()]
mas = []
buff = ''
for i in s:
  if i[0] in '+*':
    i = i[1:]
  if i[-1] in '+*':
      i = i[:-1]
  i = i.split('+')
  for m in i:
    if eval(m) == 0:
      buff = buff + m + '+'
    else:
      mas.append(buff)
      buff = ''
  mas.append(buff)
  buff = ''
print(len(max(mas, key=len)) - 1)

