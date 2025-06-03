W = [i for i in range(26, 52)]
P = [i for i in range(10, 36)]
A = []
for x in range(1, 10000):
    if (((x in P) <= (not(x in W))) or (x in A)) == 0:
        A.append(x)

print(len(A))