from itertools import *

def f(x):
     P = 35 <= x <= 55
     Q = 45 <= x <= 65
     A = a1 <= x <= a2
     return (P <= A) and ((not(A)) <= (not(Q)))
    

Ox = [y for x in [35, 55, 45, 65] for y in [x, x-0.1, x+0.1]]
m = []

for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 1 for x in Ox):
        m.append(a2 - a1)

print(round(min(m)))
