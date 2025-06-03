def g(s, p, end):
    if s >= 47:
        return p in end
    if p > max(end):
        return False
    h = [g(s + 1, p + 1, end), g(s * 2, p + 1, end)]
    return any(h) if (p + 1) % 2 == end[0] % 2 else all(h)

for s in range(1, 47):
    if g(s, 0, [3]) and not(g(s, 0, [1])):
        print(s)