
res_mas = []
for n in range(1, 26):
  s = bin(n)[2:]
  if n % 2 == 1:
    s = '10' + s + '1'
  else:
    s = '10' + s + '0111'
  res_mas.append(int(s, 2))
print(max(res_mas))
