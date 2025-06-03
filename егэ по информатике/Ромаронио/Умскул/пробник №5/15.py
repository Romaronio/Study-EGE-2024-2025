Q = [i for i in range(23, 41)]
P = [i for i in range(12, 26)]
A = []
for x in range(1, 10000):
  if (((x in P) and (not(x in Q))) <= (x in A)) == 0:
    A.append(x)

print(len(A), 23 - 12)
