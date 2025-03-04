a = [x for x in range(1, 10000)]

def f(x):
  A = x in list(range(100))
  P = x in list(range(2, 20))
  Q = x in list(range(5, 50))
  return (A <= P) and (Q <= (not A))

for x in range(1, 1000):
  if f(x) == 0:
    a.remove(x)
print(a)
