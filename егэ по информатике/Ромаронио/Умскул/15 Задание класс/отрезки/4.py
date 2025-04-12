# P = list(range(11, 29))
# Q = list(range(21, 42))
# A = list(range(1, 10000))
# for x in range(1, 10000):
#   if (((x in P) <= (x in Q)) <= (x not in A)) == 0:
#     A.remove(x)
# print(A)
# print(20 - 11)
# # ответ 10


P = [i/4 for i in range(11 * 4, 28 * 4 + 1)]
Q = [i/4 for i in range(21 * 4, 42 * 4 + 1)]
A = [i/4 for i in range(10, 1000)]
for x in range(1, 1000):
  x0 = x / 4
  if (((x0 in P) <= (x0 in Q)) <= (x0 not in A)) == 0:
    A.remove(x0)
print(A)