f = open('301_17.txt')
s = f.read()
s = s.split('\n')
k = 0
for i in range(len(s) - 1):
  m = [int(s[i]), int(s[i + 1])]
  m.sort()
  if  m[1] % 16 == m[0] or m[0] % 16 == m[0]:
    k += 1
    print(m, sum(m), k)