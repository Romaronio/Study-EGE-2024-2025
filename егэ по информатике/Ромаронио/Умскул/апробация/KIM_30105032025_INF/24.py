f = open('301_24.txt')
s = f.readline()
s = s.replace('AB', 'NN')
s = s.split('NN')
buff = ''
k = 0
res_mas = []
for x in s:
  if k < 50:
    buff += x
    k += 1
  else:
    k = 0
    res_mas.append(len(buff))
    buff = ''
print(max(res_mas))

