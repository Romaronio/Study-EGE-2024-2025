P = list(range(13, 33))
Q = list(range(15, 21))
A = [i for i in range(1, 10000)]
for x in range(1, 10000):
  if (((x in A) <= (x in P)) or (x in Q)) == 0:
    A.remove(x)
print(A)
print(32 - 13)