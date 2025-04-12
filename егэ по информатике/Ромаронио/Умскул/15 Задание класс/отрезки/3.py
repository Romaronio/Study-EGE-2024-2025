P = list(range(13, 33 + 1))
Q = list(range(22, 44 + 1))
A = []
for x in range(1, 10000):
  if ((not(x in A)) <= (((x in P) and (x in Q)) <= (x in A))) == 0:
    A.append(x)
print(A)
print(33 - 22)

