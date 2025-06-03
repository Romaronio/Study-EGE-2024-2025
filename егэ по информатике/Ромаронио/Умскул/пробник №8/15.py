W = [i for i in range(8, 18)]
P = [i for i in range(3, 12)]
A = [i for i in range(1, 1000)]
for x in range(1, 10000):
    if (((x in A) <= (x in P)) or (x in W)) == 0:
        A.remove(x)
print(A, 17 - 3)