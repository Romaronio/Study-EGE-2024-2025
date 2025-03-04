def Del(m, n):
  return n % m == 0

def notDel(m, n):
  return n % m != 0

mas = []
for a in range(1, 1000):
  A_podoshel = True
  for x in range(1, 1000):
    if ((notDel(x, a) and (Del(x, 8))) <= notDel(x, 36)) == 0:
      A_podoshel = False
      break
  if A_podoshel == True:
    mas.append(a)

print(mas)