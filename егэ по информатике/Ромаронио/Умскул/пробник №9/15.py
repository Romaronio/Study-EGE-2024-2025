from sys import *
setrecursionlimit(10000)
def f(n):
    if n == 0:
        return 1
    if n < 0:
        return n * f(n + 1)

print((f(-2024) - f(-2023) + f(-2022)) / f(-2022))