# P = list(range(2, 51))
# Q = list(range(5, 51))
# A = set()
# for x in range(1, 1000):
#   if ((A <= P) and (Q <= (not A))) == 0:
#     A.append(x)
#
# print(A)

def f(x):
  A = x in a
  P = x in P
  Q = x in Q
  return (A <= P) and (Q <= (not A))

P = list(range(2, 20))
Q = list(range(5, 51))
a = []
for x in range(1, 100):
	if f(x) == 0:
		a.append(x)
print(a)
