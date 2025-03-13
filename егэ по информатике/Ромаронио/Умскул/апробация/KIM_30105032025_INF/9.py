f = open('9.txt')
k = 0
for s in f:
  s = s.replace('\t', ' ')
  s = s.replace('\n','')
  s = s.split(' ')
  s = [int(i) for i in s]
  s.sort()
  if s[3] < s[0] + s[1] + s[2]:
    if len(set(s)) == 3:
      k += 1
print(k)
