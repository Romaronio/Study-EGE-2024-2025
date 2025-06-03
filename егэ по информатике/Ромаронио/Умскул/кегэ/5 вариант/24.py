f = open('24_319.txt')
s = f.readline()
mas = set()
buff = ''
for i in range(len(s)):
  if s[i] in '0123456789':
    buff = buff + s[i]
  else:
    mas.add(buff)
    buff = ''

res_mas = []
for i in mas:
  if i != '' and int(i) % 2 == 1:
    res_mas.append(i)

print(min(res_mas))
