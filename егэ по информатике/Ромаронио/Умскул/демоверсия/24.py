f = open('24.txt')
s = f.readline()
s = s.replace('*', 'A')
s = s.replace('-', 'A')
s = s.split('A')
S = []
for m in s:
  if m != '':
    S.append(str(int(m)))
  else:
    S.append('-')
res_mas = []
buff = ''

for i in range(len(S) - 2):
  if S[i] == '-' and S[i + 1] == '-':
    res_mas.append(buff)
    buff = ''
  if S[i] == '-' and S[i + 1] == '0' and S[i + 2] == '-':
    res_mas.append(buff)
    buff = ''
  else:
    buff += S[i]

print(len(max(res_mas, key=len)))





