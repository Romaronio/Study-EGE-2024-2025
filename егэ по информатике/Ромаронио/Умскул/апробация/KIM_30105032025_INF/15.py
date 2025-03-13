p = [x for x in range(17, 59)]
q = [x for x in range(29, 81)]
a = []
for x in range(1, 1000):
  if ((x in p) <= ((x in q) and (not(x in a)) <= (not(x in p)))) == 0:
    a.append(x)
print(len(a))
