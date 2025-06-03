f = open('9.txt')
k = 0
for s in f:
  s = s.split()
  if len(set(s)) == 5 and s.count(s[0]) <= 2 and  s.count(s[1]) <= 2 and  s.count(s[2]) <= 2 and  s.count(s[3]) <= 2 and  s.count(s[4]) <= 2 and  s.count(s[5]) <= 2 and  s.count(s[6]) <= 2:
    znach_povto = []
    ne_povtor = []
    if s.count(s[0]) == 2:
      znach_povto.append(int(s[0]))
    else:
      ne_povtor.append(int(s[0]))
    if s.count(s[1]) == 2:
      znach_povto.append(int(s[1]))
    else:
      ne_povtor.append(int(s[1]))
    if s.count(s[2]) == 2:
      znach_povto.append(int(s[2]))
    else:
      ne_povtor.append(int(s[2]))
    if s.count(s[3]) == 2:
      znach_povto.append(int(s[3]))
    else:
      ne_povtor.append(int(s[3]))
    if s.count(s[4]) == 2:
      znach_povto.append(int(s[4]))
    else:
      ne_povtor.append(int(s[4]))
    if s.count(s[5]) == 2:
      znach_povto.append(int(s[5]))
    else:
      ne_povtor.append(int(s[5]))
    if s.count(s[6]) == 2:
      znach_povto.append(int(s[6]))
    else:
      ne_povtor.append(int(s[6]))

    if sum(znach_povto) / len(znach_povto) >= sum(ne_povtor) / len(ne_povtor):
      k += 1

print(k)