from sys import *
setrecursionlimit(10000)

def f(n):
    if n < 31:
        return n
    if n >= 31:
        return (n - 13) * f(n - 9)

print((f(36924) - 2025 * f(36913)) / f(36900))