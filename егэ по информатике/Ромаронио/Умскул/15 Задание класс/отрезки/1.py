P = list(range(3, 18 + 1))
Q = list(range(11, 24 + 1))
A = []
for x in range(1, 10000):
  if (((x in P) and (x in Q)) <= (x in A)) == 0:
    A.append(x)
print(A, 18 - 11)