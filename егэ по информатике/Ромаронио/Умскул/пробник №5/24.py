f = open('24.txt')
s = f.readlines()
always_strok = []
best_len = 0
povtor = []
for i in s:
  buff = ''
  print(buff)
  for m in range(len(i)):
    if i[m] == i[m - 1]:
      buff = buff + i[m]
    else:
      if best_len < len(buff):
        best_len = len(buff)
        povtor = []
      elif best_len == len(buff):
        povtor.append(len(buff))
  always_strok.append([best_len, povtor])
  best_len = 0
  povtor = []

print(max(always_strok))
