f = open('24_22362.txt')
s = f.readline()
mas = []
mas2 = []
for i in 'CDEFGHIJKLMNOPQRSTUVWXYZ':
  s = s.replace(i, 'A')

s = s.split('A')
for i in s:
  if i != '':
    m = str(int(i, 12))
    mas2.append(m)

print(mas2)
print(len(max(mas2, key=len)))

