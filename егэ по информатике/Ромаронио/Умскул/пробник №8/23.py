def f(start, end):
    if start == end:
        return 1
    if start > end or start == 12 or start == 24:
        return 0
    if start < end:
        return f(start + 1, end) + f(start + 2, end) + f((start * 3) - 1, end)
print(f(1, 20) * f(20, 40) * f(40, 50))