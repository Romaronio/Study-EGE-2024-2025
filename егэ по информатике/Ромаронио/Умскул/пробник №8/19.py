def g(s, p, end):
    if s < 19:
        return p in end
    if p > max(end):
        return False
    h = [g(s - 2, p + 1, end), g(s - 3, p + 1, end)]
    if s % 2 == 0:
        h.append(g(s / 2, p + 1, end))
    if s % 3 == 0:
        h.append(g((s / 3) * 2, p + 1, end))
    return any(h) if ((p + 1) % 2) == (end[0] % 2) else all(h)

for s in range(19, 100):
    if g(s, 0, [2]) and not(g(s, 0, [1])):
        print(s)
