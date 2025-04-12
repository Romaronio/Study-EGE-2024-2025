P = list(range(15, 41))
Q = list(range(21, 64))
A = []
for x in range(1, 10000):
  if ((x in P) <= (((x in Q) and (not(x in A))) <= (not(x in P)))) == 0:
    A.append(x)

print(A)
print(40-21)
