def Del(n, m):
  return n % m == 0

def notDel(n, m):
  return n % m != 0

mas_a = []
for A in range(1, 1000):
  for x in range(1, 1000):
    if (Del(A, 9) and (Del(280, x) <= (notDel(A, x) <= notDel(730, x)))) == 0:
      break
  else:
    mas_a.append(A)
print(min(mas_a))