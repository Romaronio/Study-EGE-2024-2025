P = list(range(16, 59 + 1))
Q = list(range(27, 71 + 1))
A = []
for x in range(1, 10000):
  if ((not(x in A)) <= ((x in P) <= (not(x in Q)))) == 0:
    A.append(x)
print(A)
print(59 - 27)
