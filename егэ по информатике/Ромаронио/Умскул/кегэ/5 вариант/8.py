k = 0
for x in range(1000000, 10000000):
  x = str(x)
  if (x.count('2') + x.count('4') + x.count('6') + x.count('8') + x.count('0')) == 2:
    k += 1
print(k)